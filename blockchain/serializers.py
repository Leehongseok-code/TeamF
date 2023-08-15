#product/serializers.py
from rest_framework import serializers
from .models import CoinNews, Subscribers

class CoinNewsSerializer(serializers.ModelSerializer) :
    class Meta :
        model = CoinNews    # product 모델 사용
        fields = '__all__'            # 모든 필드 포함

class SubscribersSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Subscribers    # product 모델 사용
        fields = '__all__'            # 모든 필드 포함