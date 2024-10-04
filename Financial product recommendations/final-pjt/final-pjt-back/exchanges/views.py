from django.shortcuts import render
from django.conf import settings
import requests
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Exchanges
from .serializers import ExchangesSerializer

date = '20240517'

# 환율 저장
@api_view(['GET'])
def exchanges_save(request):
    URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': settings.EXCHANGE_API_KEY,
        'searchdate': date,
        'data': 'AP01'
    }
    response = requests.get(URL, params=params).json()
    for obj in response:
        if '100' not in obj['cur_unit']:
            save_data = {
                'cur_unit': obj['cur_unit'],
                'cur_nm': obj['cur_nm'],
                'deal_bas_r': float(obj['deal_bas_r'].replace(',', ''))
            }
        else:
            save_data = {
                'cur_unit': obj['cur_unit'][:3],
                'cur_nm': obj['cur_nm'],
                'deal_bas_r': round(float(obj['deal_bas_r'].replace(',', ''))*0.01, 4)
            }
        serializer = ExchangesSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'response': response})

@api_view(['GET'])
def exchanges(request):
    if request.method == 'GET':
        exchanges = get_list_or_404(Exchanges)
        serializers = ExchangesSerializer(exchanges, many=True)
        return Response(serializers.data)
    # Exchange = get_object_or_404(Exchanges, cur_unit=request.data['cur_unit'])
    # if request.method == 'GET':
    #     serializer = ExchangesSerializer(Exchange)
    #     return Response(serializer.data)