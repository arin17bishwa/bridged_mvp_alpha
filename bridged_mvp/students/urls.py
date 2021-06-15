from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    play_view,
    registration_view,
    activate,
    user_info_view,
    )

app_name = 'students'

urlpatterns = [
    path('', play_view, name='homepage'),
    path('register/',registration_view, name='homepage'),
    path('login/',obtain_auth_token,name='login'),
    path('userinfo/', user_info_view, name='userinfo'),

    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),

]
