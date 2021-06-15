from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from .utils import send_conf_mail,account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import sys


from .serializers import RegistrationSerializer,UserSerializer

# Create your views here.


@api_view(['GET',])
def play_view(request):
    return Response(data={'msg':'hello world'})


@api_view(['POST', ])
@permission_classes([IsAdminUser,])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['username'] = account.username
        data['email']=account.email
        data['msg'] = 'Successfully registered'
        _=send_conf_mail(request=request,user=account,email=data['email'])
        token=Token.objects.get(user=account).key
        data['token']=token
        status_code=status.HTTP_201_CREATED
    else:
        data=serializer.errors
        status_code=status.HTTP_400_BAD_REQUEST
    return Response(data,status=status_code)


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def user_info_view(request):
    user=request.user
    serializer = UserSerializer(user)
    data={}
    try:
        data['data']=serializer.data
        data['status']=1
        status_code=status.HTTP_200_OK
    except Exception as e:
        data['error']=e
        data['status']=0
        status_code=status.HTTP_400_BAD_REQUEST

    return Response(data=data,status=status_code)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('account:create_profile', slug=str(user.registration_no).lower())
        return HttpResponse('Account activated!')

    else:
        return HttpResponse('Activation link is invalid!')