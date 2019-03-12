from django.urls import path
from .views import HoraExtraListList, HoraExtraEdit

urlpatterns = [
    path('', HoraExtraListList.as_view(), name='list_hora_extra'),
    # path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='update_hora_extra'),
    # path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
]
