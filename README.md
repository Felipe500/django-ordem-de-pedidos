# django-ordem-de-pedidos
Gerenciar ordens de pedidos para entregar ( origin : PERFIL DO CRIADOR DO CURSO NO YOUTUBE https://github.com/divanov11/crash-course-CRM )

# configuração do app
PIP INSTALL REQUIREMENTS:

    Django                            3.2.6  (V3 DJANGO)
    django-ckeditor                   6.1.0  (RICH TEXT)
    django-crispy-forms               1.11.2 (FORMS DINÂMICOS
    django-filter                     2.4.0 ( FILTROS)
    django-resized                    0.3.11 (OPCIONAL- AINDA VOU IMPLEMENTÁ-LO)

TERMINAL - CMD:


    1 - django-admin startproject 'NOME_PROJETO'
    2 - cd 'NOME_PROJETO'

# A sub-pasta do projeto NOME_PROJETO será a raíz para nosso site:

  __init__.py é um arquivo em branco que instrui o Python a tratar esse diretório como um pacote Python.
    
   settings.py contém todas as definições do website. É onde nós registramos qualquer aplicação que criarmos,a localização de nossos arquivos estáticos,             configurações de banco de dados etc. 
    
  urls.py define os mapeamentos de URL para visualização do site. Mesmo que esse arquivo possa conter todo o código para mapeamento de URL, é mais comum delegar      apenas o mapeamento para aplicativos específicos, como será visto mais adiante.
  
  wsgi.py é usado para ajudar na comunicação entre seu aplicativo Django e o web server. Você pode tratar isso como um boilerplate.

  O script manage.py é usado para criar aplicações, trabalhar com bancos de dados, e iniciar o webserver de desenvolvimento. 

3 - Dentro da pasta do projeto faça um clone do app no github com o comando:  


     git clone https://github.com/Felipe500/django-ordem-de-pedidos.git


     INSTALLED_APPS = [
    ***
    'django-ordem-de-pedidos.apps.AccountsConfig',
    'django_filters',
    'ckeditor'
    ***
    ]
    
