from django.urls import path
from .views import HoraExtraListList

urlpatterns = [
    path('', HoraExtraListList.as_view(), name='list_hora_extra'),
    # path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    # path('editar/<int:pk>', FuncionarioEdit.as_view(), name='update_funcionario'),
    # path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
]
