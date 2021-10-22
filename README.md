# django-ordem-de-pedidos
Gerenciar ordens de pedidos para entregar ( origin : PERFIL DO CRIADOR DO CURSO NO YOUTUBE https://github.com/divanov11/crash-course-CRM )
# Gerenciar ordens de pedidos para entregar. O admin do sistema recebe a lista de pedido para entrega para um certo cliente, e o cliente no mesmo sistema realiza uma consulta para saber como está o andamento da sua entrega de seu pedido.  

# DASHBOARD DO ADMIN - PAINEL DE CONTROLE DE ORDEM DE PEDIDOS

![alt text](https://github.com/Felipe500/django-ordem-de-pedidos/blob/649e390cf9a872274390630229a845faf5042d19/tela%20admin%201.png?raw=true)

# TELA DE DETALHE DOS PEDIDOS DO CLIENTE

![alt text](https://github.com/Felipe500/django-ordem-de-pedidos/blob/main/tela%20admin%204%20-%20detalhe%20cliente.png?raw=true)


# LISTAGEM DE PRODUTOS

![alt text](https://github.com/Felipe500/django-ordem-de-pedidos/blob/649e390cf9a872274390630229a845faf5042d19/tela%20admin%202.png?raw=true)


# ADICIONAR PEDIDO DO CLIENTE AO SISTEMA

![alt text](https://github.com/Felipe500/django-ordem-de-pedidos/blob/649e390cf9a872274390630229a845faf5042d19/tela%20admin%205%20-%20adicionar%20pedido%20ao%20cliente.png?raw=true)


# ATUALIZAR PEDIDO DO CLIENTE

![alt text](https://github.com/Felipe500/django-ordem-de-pedidos/blob/649e390cf9a872274390630229a845faf5042d19/tela%20admin%203.png?raw=true)


# ARÉA DO CLIENTE
# DASHBOARD - PAINEL DO CLIENTE

![alt text](https://github.com/Felipe500/django-ordem-de-pedidos/blob/649e390cf9a872274390630229a845faf5042d19/tela%20cliente%20-%201.png?raw=true)


# CONFIGURAR PERFIL DO CLIENTE
![alt text](https://github.com/Felipe500/django-ordem-de-pedidos/blob/649e390cf9a872274390630229a845faf5042d19/tela%20cliente%20-%202%20PEFIL%20USUARIO.png?raw=true)

# configuração do app
PIP INSTALL REQUIREMENTS:

    Django                            3.2.6  (V3 DJANGO)
    django-ckeditor                   6.1.0  (RICH TEXT)
    django-crispy-forms               1.11.2 (FORMS DINÂMICOS
    django-filter                     2.4.0 ( FILTROS)
    django-resized                    0.3.11 (OPCIONAL- AINDA VOU IMPLEMENTÁ-LO)

1° PASSO NO TERMINAL - CMD:


    1.1 - django-admin startproject 'NOME_PROJETO'
    1.2 - cd 'NOME_PROJETO'

# A sub-pasta do projeto NOME_PROJETO será a raíz para nosso site:

  __init__.py é um arquivo em branco que instrui o Python a tratar esse diretório como um pacote Python.
    
   settings.py contém todas as definições do website. É onde nós registramos qualquer aplicação que criarmos,a localização de nossos arquivos estáticos,             configurações de banco de dados etc. 
    
  urls.py define os mapeamentos de URL para visualização do site. Mesmo que esse arquivo possa conter todo o código para mapeamento de URL, é mais comum delegar      apenas o mapeamento para aplicativos específicos, como será visto mais adiante.
  
  wsgi.py é usado para ajudar na comunicação entre seu aplicativo Django e o web server. Você pode tratar isso como um boilerplate.

  O script manage.py é usado para criar aplicações, trabalhar com bancos de dados, e iniciar o webserver de desenvolvimento. 

2 - Dentro da pasta do projeto('NOME_PROJETO') faça um clone do app no github com o seguinte comando e depois renomeie a pasta para 'accounts':  

     #clonar repositório no github
     git clone https://github.com/Felipe500/django-ordem-de-pedidos.git
     
     #renomear a pasta
     mv django-ordem-de-pedidos accounts
   
3 - Agora entre na pasta do projeto principal e procure o arquivo de configuração do django 'settings.py', e faça as seguintes alterações: 
     
     #cabeçalho do arquivo
     import os
    
    #----------------------------
    
     INSTALLED_APPS = [
    ***
    'accounts.apps.AccountsConfig',
    'django_filters',
    'ckeditor'
    ***
    ]
    
    #--------------------------
    
    STATIC_URL = '/static/'

    MEDIA_URL = '/images/'

    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
    ]

    MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
    
4 - no arquivo urls, adicione as rotas para a aplicação 'accounts' e o caminho para os arquivos estaticos da aplicação:
    
    from django.contrib import admin
    from django.urls import path, include

    from django.conf.urls.static import static
    from django.conf import settings


    urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('accounts.urls')),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
5 - procure o arquivo manage.py e execute o terminal na pasta deste arquivo, e siga com os comandos para criar as tabelas do banco de dados e criação do 'super user', ou usuario admin:
    
    #criar banco de dados
    python3 manage.py migrate
    
    #criar um usuario admin
    python3 manage.py createsuperuser
    
