from django.shortcuts import render
from django.views.generic import ListView
from .models import RegistroHoraExtra


class HoraExtraListList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)

