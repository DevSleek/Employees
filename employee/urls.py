from django.urls import path
from .views import get_employees


urlpatterns = [
    path('get_employees', get_employees, name='get_employees'),
]
