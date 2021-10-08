
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', inicio, name = 'home'),

    path('registrar/', register_page, name = 'registrar'),
    path('login/', login_page , name='logar'),
    path('sair/', sair_conta , name='logout'),

    path('produtos/', prod, name = 'produtos'),
    path('cliente/<str:id>/', cliente , name='clientes'),
    path('usuario/', pagina_usuario, name="user-page"),

    path('novo_pedido/<str:pk>/', fazer_pedido , name='novo_pedido'),
    path('atualizar_pedido/<str:id>/', atualizar_pedido, name="atualiza_pedido"),
    path('remover_pedido/<str:id>/', remover_pedido, name="remove_pedido"),
    
    path('perfil_user/', perfil_usuario, name="perfil_usuario")

]