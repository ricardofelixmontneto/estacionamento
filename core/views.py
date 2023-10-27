import json

from django.shortcuts import render
from django.http import HttpResponse

from .models import Pessoa, Veiculo

def home(request):
    return HttpResponse('Ola Mundo')


def lista_pessoas(request):
    pessoas = [p.nome for p in Pessoa.objects.all()]

    return HttpResponse(json.dumps({'pessoas': pessoas}))


def lista_veiculos(request):
    veiculos = [v.placa for v in Veiculo.objects.all()]
    return HttpResponse(json.dumps({'veiculos': veiculos}))


def lista_veiculos(request):
    veiculos = [v.placa for v in Veiculo.objects.all()]
    return HttpResponse(json.dumps({'veiculos': veiculos}))
