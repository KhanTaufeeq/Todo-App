from . models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from secrets import token_hex
import datetime 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id','name','password', 'token','token_expires','email')


class UserSignUpSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required = True)
    email = serializers.EmailField(required = True)
    password = serializers.CharField(write_only=True, required = True)
    token = serializers.CharField(read_only=True)
    token_expires = serializers.DateTimeField(read_only=True)

    class Meta:
        model=User 
        fields = ('id','name','email','password', 'token', 'token_expires')

    def create(self,validated_data):
        if User.objects.filter(email = validated_data['email']).exists():
            raise serializers.ValidationError({'email':['The email is already taken']})
        
        validated_data['password'] = make_password(validated_data['password'])

        validated_data['token'] = token_hex(30)
        validated_data['token_expires'] = datetime.datetime.now() + datetime.timedelta(days=7)

        return super().create(validated_data)

class UserSignInSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(write_only = True)
    password = serializers.CharField(write_only = True)
    token = serializers.CharField(read_only = True)
    token_expires = serializers.DateTimeField(read_only = True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'token', 'token_expires')


    def create(self, validated_data):
        user = User.objects.filter(email=validated_data['email'])
        
        if len(user)>0 and check_password(validated_data['password'], user[0].password):

            user[0].token = token_hex(30)
            user[0].token_expires = datetime.datetime.now() + datetime.timedelta(days=7)
            user[0].save() 

            return user [0]
        
        else:
            raise serializers.ValidationError({'email':'The email or password is wrong'})

