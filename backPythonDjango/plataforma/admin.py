from django.contrib import admin
from .models import Parceiro, TipoContrato, Acompanhamento, Contrato

admin.site.register(Parceiro)
admin.site.register(TipoContrato)
admin.site.register(Acompanhamento)
admin.site.register(Contrato)
