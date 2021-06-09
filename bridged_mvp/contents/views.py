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

from .serializers import (
    ContentSerializer,
)

from .models import (
    Content,
)

# Create your views here.


class AllContentListView(ListAPIView):
    queryset = Content.objects.order_by('name')
    serializer_class = ContentSerializer
    permission_classes = (IsAuthenticated,)
