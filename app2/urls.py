from django.urls import path
from app2.views import *
app_name='anushka'

urlpatterns=[
    path('pashupathi/',pashupathi,name='pashupathi'),
]