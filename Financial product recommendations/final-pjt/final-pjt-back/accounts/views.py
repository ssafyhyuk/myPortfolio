from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from products.models import DepositProducts, SavingProducts
from products.serializers import DepositProductsSerializer, SavingProductsSerializer
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_products_list(request):
    user = request.user
    serializer = DepositProductsSerializer(user.deposit_join_products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_products_list(request):
    user = request.user
    serializer = SavingProductsSerializer(user.saving_join_products, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)