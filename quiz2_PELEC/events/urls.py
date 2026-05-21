from django.urls import path
from .views import register_event

urlpatterns = [
    path('', register_event, name='register_event'),
]