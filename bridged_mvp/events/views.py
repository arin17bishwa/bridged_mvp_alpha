from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils import timezone
from .models import Event
from .serializers import EventSerializer


# Create your views here.


class EventsListView(ListAPIView):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

    ordering = ('start_time',)

    def get_queryset(self):
        size = self.kwargs.get('size')
        qs = Event.objects.filter(end_time__gte=timezone.now())
        if size is None:
            upcoming = qs.earliest('start_time')
            final_qs = [upcoming]
        else:
            final_qs = qs.order_by('start_time')[:size]

        return final_qs
