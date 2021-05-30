from django.urls import path

from .views import (
    EventsListView,
)

app_name = 'events'

urlpatterns = [
    path('upcoming/', EventsListView.as_view(), {'size': None}, name='upcoming_event'),
    path('all-events/', EventsListView.as_view(), {'size': 12}, name='upcoming_event'),

]
