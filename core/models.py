import math

from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.name = models.ForeignKey(Marca, on_delete=models.CASCADE, default=1)
    placa = models.CharField(max_length=7)
    propeietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default=1)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()

    def __str__(self):
        return f'{self.marca} {self.placa}'
    

class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f'hora R$ {self.valor_hora} - mês R$ {self.valor_mes}'
    

class MovRotativo(models.Model):
    entrada = models.DateTimeField(auto_now=False)
    saida = models.DateTimeField(auto_now=False)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)
    
    def horas_total(self):
        return math.ceil((self.saida - self.entrada).total_seconds()/3600)

    def total(self):
        return self.valor_hora * 2

    def __str__(self) -> str:
        return self.veiculo.placa
    

class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.veiculo} - {str(self.inicio)}'
    

class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f'{str(self.mensalista)} - {str(self.total)}'