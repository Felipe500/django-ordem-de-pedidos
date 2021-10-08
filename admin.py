from django.contrib import admin

# Register your models here.
from .models import Cliente, Tag, Produto, Pedido

admin.site.register(Cliente)

admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(Tag)