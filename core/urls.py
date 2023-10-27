from django.urls import re_path
from .views import home, lista_pessoas, lista_veiculos

urlpatterns = [
        re_path('^$', home, name='core_home'), # https://locahost:8000/core/
        re_path('^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
        re_path('^veiculos/$', lista_veiculos, name='core_lista_veiculos')
]