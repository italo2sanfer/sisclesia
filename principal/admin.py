from django.contrib import admin

from .models import Pessoa, Unidade, Ministerio, Cargo, Participacao

admin.site.register(Pessoa)
admin.site.register(Unidade)
admin.site.register(Ministerio)
admin.site.register(Cargo)
admin.site.register(Participacao)

