from django.urls import path

from .views import (
    EventsListView,
    TestimonialListView,
)

app_name = 'events'

urlpatterns = [
    path('upcoming/', EventsListView.as_view(), {'size': None}, name='upcoming_event'),
    path('all-events/', EventsListView.as_view(), {'size': 12}, name='event'),
    path('testimonials/',TestimonialListView.as_view(),name='card_testimonials'),
    path('testimonials/all/', TestimonialListView.as_view(),{'size':'all'}, name='all_testimonials'),

]
