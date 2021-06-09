from django.urls import path

from .views import (
    AllContentListView,
)

app_name='contents'

urlpatterns = [
    path('',AllContentListView.as_view(),name='all_contents'),

]