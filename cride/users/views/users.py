from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cride.users.serializers import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer, AccountVerificationSerializer

class UserLoginAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token,
        }
        return Response(data, status=status.HTTP_201_CREATED)

class UserSignUpAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

class UserVerificationAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulation, now go share some rides!'}
        return Response(data, status=status.HTTP_200_OK)