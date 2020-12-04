from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.models import add_data
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],email=validated_data['email'],password=validated_data['password'])
        
        return user

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = add_data
        fields = "__all__"


