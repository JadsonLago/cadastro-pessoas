from http.client import ImproperConnectionState
from unicodedata import name
from django.urls import path
from .views import ListaPessoaView

urlpatterns =[
    path('',ListaPessoaView.as_view(), name='pessoa.index')
]
