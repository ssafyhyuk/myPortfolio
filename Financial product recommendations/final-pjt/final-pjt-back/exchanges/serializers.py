from rest_framework import serializers
from .models import Exchanges

class ExchangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchanges
        fields = '__all__'