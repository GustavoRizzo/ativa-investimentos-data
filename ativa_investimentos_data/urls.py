from django.urls import path

from .views import Home

app_name = 'ativa_investimentos_data'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
