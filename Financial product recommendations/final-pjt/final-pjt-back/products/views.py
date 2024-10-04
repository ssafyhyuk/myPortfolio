from django.shortcuts import render
from django.conf import settings
import requests, datetime
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, Answer
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer, AnswerSerializer
from django.core import serializers
from django.contrib.auth import get_user_model

from openai import OpenAI


BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'
dict_FinGrp = {'020000': '은행', '030200': '여신전문', '030300': '저축은행', '050000': '보험', '060000': '금융투자'}
dict_JoinDeny = {1: '제한없음', 2: '서민전용', 3: '일부제한'}

def end_day(text):
    if text == None:
        return datetime.date(9999, 12, 31).strftime("%Y-%m-%d")
    else:
        return datetime.date(int(text[:4]), int(text[4:6]), int(text[6:])).strftime("%Y-%m-%d")

# 정기예금
## 정기예금 데이터 저장
@api_view(['GET'])
def deposit_products_save(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.PRODUCT_API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    for li in response['result']['baseList']:
        save_data = {
            'topFinGrp': dict_FinGrp[params['topFinGrpNo']],
            'dcls_month': li['dcls_month'],
            'fin_co_no': li['fin_co_no'],
            'fin_prdt_cd': li['fin_prdt_cd'],
            'kor_co_nm': li['kor_co_nm'],
            'fin_prdt_nm': li['fin_prdt_nm'],
            'join_way': li['join_way'],
            'mtrt_int': li['mtrt_int'],
            'spcl_cnd': li['spcl_cnd'],
            'join_deny': dict_JoinDeny[int(li['join_deny'])],
            'join_member': li['join_member'],
            'etc_note': li['etc_note'],
            'max_limit': li['max_limit'],
            'dcls_strt_day': datetime.date(int(li['dcls_strt_day'][:4]), int(li['dcls_strt_day'][4:6]), int(li['dcls_strt_day'][6:])).strftime("%Y-%m-%d"),
            'dcls_end_day': end_day(li['dcls_end_day']),
            'fin_co_subm_day': datetime.datetime(int(li['fin_co_subm_day'][:4]), int(li['fin_co_subm_day'][4:6]), int(li['fin_co_subm_day'][6:8]), int(li['fin_co_subm_day'][8:10]), int(li['fin_co_subm_day'][10:])).strftime("%Y-%m-%d %H:%M")
        }
        serializer = DepositProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    for li in response['result']['optionList']:
        temp = DepositProducts.objects.get(fin_prdt_cd = li['fin_prdt_cd'])
        save_data = {
            'product': temp.id,
            'fin_prdt_cd': li['fin_prdt_cd'],
            'intr_rate_type_nm': li['intr_rate_type_nm'],
            'save_trm': li['save_trm'],
            'intr_rate': li['intr_rate'],
            'intr_rate2': li['intr_rate2']            
        }
        serializer = DepositOptionsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'response': response})

## 정기예금 전체 LIST
@api_view(['GET'])
def deposit_products(request):
    if request.method == 'GET':
        deposits = get_list_or_404(DepositProducts)
        serializer = DepositProductsSerializer(deposits, many=True)
        return Response(serializer.data)

## 정기예금 상품 DETAIL
@api_view(['GET'])
def deposit_products_detail(request, fin_prdt_cd):
    if request.method == 'GET':
        deposit = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
        serializer = DepositProductsSerializer(deposit)
        return Response(serializer.data)

## 정기예금 옵션 DETAIL
@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    if request.method == 'GET':
        options = DepositOptions.objects.filter(fin_prdt_cd = fin_prdt_cd)
        serializer = DepositOptionsSerializer(options, many=True)
        return Response(serializer.data)
    
## 정기예금 가입
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_products_join(request, fin_prdt_cd):
    if request.method == 'GET':
        deposit = get_object_or_404(DepositProducts, fin_prdt_cd = fin_prdt_cd)
        user = request.user
        # user = get_object_or_404(get_user_model(), pk=user_pk)
        deposit.deposit_join_users.add(user)
        return Response(status=status.HTTP_201_CREATED)
    
## 정기예금 해지
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_products_remove(request, fin_prdt_cd):
    if request.method == 'GET':
        deposit = get_object_or_404(DepositProducts, fin_prdt_cd = fin_prdt_cd)
        user = request.user
        deposit.deposit_join_users.remove(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


# 적금
## 적금 데이터 저장
@api_view(['GET'])
def saving_products_save(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth': settings.PRODUCT_API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    for li in response['result']['baseList']:
        save_data = {
            'topFinGrp': dict_FinGrp[params['topFinGrpNo']],
            'dcls_month': li['dcls_month'],
            'fin_co_no': li['fin_co_no'],
            'fin_prdt_cd': li['fin_prdt_cd'],
            'kor_co_nm': li['kor_co_nm'],
            'fin_prdt_nm': li['fin_prdt_nm'],
            'join_way': li['join_way'],
            'mtrt_int': li['mtrt_int'],
            'spcl_cnd': li['spcl_cnd'],
            'join_deny': dict_JoinDeny[int(li['join_deny'])],
            'join_member': li['join_member'],
            'etc_note': li['etc_note'],
            'max_limit': li['max_limit'],
            'dcls_strt_day': datetime.date(int(li['dcls_strt_day'][:4]), int(li['dcls_strt_day'][4:6]), int(li['dcls_strt_day'][6:])).strftime("%Y-%m-%d"),
            'dcls_end_day': end_day(li['dcls_end_day']),
            'fin_co_subm_day': datetime.datetime(int(li['fin_co_subm_day'][:4]), int(li['fin_co_subm_day'][4:6]), int(li['fin_co_subm_day'][6:8]), int(li['fin_co_subm_day'][8:10]), int(li['fin_co_subm_day'][10:])).strftime("%Y-%m-%d %H:%M")
        }
        serializer = SavingProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    for li in response['result']['optionList']:
        temp = SavingProducts.objects.get(fin_prdt_cd = li['fin_prdt_cd'])
        save_data = {
            'product': temp.id,
            'fin_prdt_cd': li['fin_prdt_cd'],
            'intr_rate_type_nm': li['intr_rate_type_nm'],
            'rsrv_type_nm': li['rsrv_type_nm'],
            'save_trm': li['save_trm'],
            'intr_rate': li['intr_rate'],
            'intr_rate2': li['intr_rate2']            
        }
        serializer = SavingOptionsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'response': response})

## 적금 전체 LIST
@api_view(['GET'])
def saving_products(request):
    if request.method == 'GET':
        savings = get_list_or_404(SavingProducts)
        serializer = SavingProductsSerializer(savings, many=True)
        return Response(serializer.data)

## 적금 상품 DETAIL
@api_view(['GET'])
def saving_products_detail(request, fin_prdt_cd):
    if request.method == 'GET':
        saving = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
        serializer = SavingProductsSerializer(saving)
        return Response(serializer.data)

## 적금 옵션 DETAIL
@api_view(['GET'])
def saving_products_options(request, fin_prdt_cd):
    if request.method == 'GET':
        options = SavingOptions.objects.filter(fin_prdt_cd = fin_prdt_cd)
        serializer = SavingOptionsSerializer(options, many=True)
        return Response(serializer.data)
    
## 적금 가입
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_products_join(request, fin_prdt_cd):
    if request.method == 'GET':
        saving = get_object_or_404(SavingProducts, fin_prdt_cd = fin_prdt_cd)
        user = request.user
        # user = get_object_or_404(get_user_model(), pk=user_pk)
        saving.saving_join_users.add(user)
        return Response(status=status.HTTP_201_CREATED)
    
## 적금 해지
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_products_remove(request, fin_prdt_cd):
    if request.method == 'GET':
        saving = get_object_or_404(SavingProducts, fin_prdt_cd = fin_prdt_cd)
        user = request.user
        saving.saving_join_users.remove(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# 상품 추천
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def products_recommend(request):
    deposits = DepositProducts.objects.all()
    deposits_serializer = DepositProductsSerializer(deposits, many=True)

    deposits_options = DepositOptions.objects.all()
    deposits_options_serializer = DepositOptionsSerializer(deposits_options, many=True)

    savings = SavingProducts.objects.all()
    savings_serializer = SavingProductsSerializer(savings, many=True)

    savings_options = SavingOptions.objects.all()
    savings_options_serializer = SavingOptionsSerializer(savings_options, many=True)

    
    
    
    
    client = OpenAI(
        api_key = settings.GPT_API_KEY
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "이제부터 너는 금융상품 데이터를 제공해주고 추천해주는 Q&A 챗봇이야. 너의 이름은 쿄야마 카즈사이고, 말 끝마다 냥을 붙이는 냥체를 사용해서 귀엽게 말해야 돼!"
            },
            {
                "role": "system",
                "content": f"클라이언트의 연봉은 대략 {request.user.income}이고 보유재산은 대략 {request.user.asset}이야."
            },
            #{
            #    "role": "system",
            #    "content": f"클라이언트의 연봉은 대략 {request.user.income}이고 보유재산은 대략 {request.user.asset}이야. 현재 저장되어있는 정기예금 상품 데이터는 {deposits_serializer.data}이고 정기예금 상품의 옵션 데이터는 {deposits_options_serializer.data}야. 현재 저장되어있는 적금 상품 데이터는 {savings_serializer.data}이고 적금 상품의 옵션 데이터는 {savings_options_serializer.data}야."
            #},
            #{
            #    "role": "system",
            #    "content": f"현재 저장되어있는 정기예금 상품 데이터는 {deposits_serializer.data}이고 정기예금 상품의 옵션 데이터는 {deposits_options_serializer.data}야."
            #},
            #{
            #    "role": "system",
            #    "content": f"현재 저장되어있는 적금 상품 데이터는 {savings_serializer.data}이고 적금 상품의 옵션 데이터는 {savings_options_serializer.data}야."
            #},
            {
                "role": "user",
                "content": request.data.get('question')
            }
        ],
        model="gpt-3.5-turbo"
    )
    save_data = {
        'answer': chat_completion.choices[0].message.content
    }
    serializer = AnswerSerializer(data=save_data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

