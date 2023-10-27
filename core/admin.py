from django.contrib import admin

from .models import (Marca, Veiculo, 
                     Pessoa, Parametros,
                     Mensalista, MovRotativo, MovMensalista)


# Personalizando a página de admin do Model MovRotativo
class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('entrada', 'saida', 'valor_hora', 'veiculo', 
                    'total', 'horas_total', 'pago')


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = (
                    'mensalista', 'dt_pgto', 'total'
                    )

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin) # Registrando o model que personaliza o Admin do MovRotativo