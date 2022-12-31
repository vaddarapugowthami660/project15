from django.urls import path
from app1.views import *
app_name='bujji'

urlpatterns=[
    path('arundhathi/',arundhathi,name='arundhathi'),
]