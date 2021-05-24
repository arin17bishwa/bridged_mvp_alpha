from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    play_view,
    registration_view,
    activate,
    )

app_name = 'students'

urlpatterns = [
    path('', play_view, name='homepage'),
    path('register/',registration_view, name='homepage'),
    path('login/',obtain_auth_token,name='login'),

    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),

]
