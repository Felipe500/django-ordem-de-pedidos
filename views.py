from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *

from .filters import OrderFilter

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from .forms import OrderForm, CreateUserForm, ClienteForm
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def register_page(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Registrado a conta ' + username)

			return redirect('logar')
		

	context = {'form':form}
	return render(request, 'accounts/register.html', context)


	
@unauthenticated_user
def login_page(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Usuário ou senha estão errados')

	context = {}		
	return render(request,'accounts/login.html')

def sair_conta(request):
	logout(request)
	return redirect('logar')



@login_required(login_url='logar')
@admin_only
def inicio(request):
	Pedidos = Pedido.objects.all()
	Clientes = Cliente.objects.all()

	total_Clientes = Clientes.count()

	total_Pedidos = Pedidos.count()

	entregues = Pedidos.filter(status='Entregue').count()
	pendentes = Pedidos.filter(status='Pendente').count()

	context = {'pedidos':Pedidos, 'Clientes':Clientes,
	'total_Cliente':total_Clientes,'total_Pedidos':total_Pedidos,'entregues':entregues,
	'pendentes':pendentes }
	return render(request, 'accounts/dashboard.html',context)


@login_required(login_url='logar')
@allowed_users(allowed_roles=['cliente'])
def pagina_usuario(request):
	pedidos = request.user.cliente.pedido_set.all()

	total_Pedidos = pedidos.count()

	entregues = pedidos.filter(status='Entregue').count()
	pendentes = pedidos.filter(status='Pendente').count()

	print('ORDERS:', pedidos)
	myFilter = OrderFilter(request.GET, queryset=pedidos)
	pedidos = myFilter.qs

	context = {'pedidos':pedidos, 
	'total_Pedidos':total_Pedidos,'entregues':entregues,
	'pendentes':pendentes ,'myFilter':myFilter}
	
	return render(request, 'accounts/pagina_usuario.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['cliente'])
def perfil_usuario(request):
	

	cliente = request.user.cliente
	form = ClienteForm(instance=cliente)

	if request.method == 'POST':
		form = ClienteForm(request.POST, request.FILES,instance=cliente)
		if form.is_valid():
			form.save()


	context = {'form':form}

	
	return render(request, 'accounts/perfil_user.html', context)

@login_required(login_url='logar')
@allowed_users(allowed_roles=['admin'])
def prod(request):
	produtos = Produto.objects.all()
	return render(request, 'accounts/produtos.html', {'produtos':produtos})



@login_required(login_url='logar')
@allowed_users(allowed_roles=['admin'])
def cliente(request, id):
	id_cliente = Cliente.objects.get(id=id)

	#-- buscar todos os pedidos onde o id do cliente for marcado
	pedidos = id_cliente.pedido_set.all()
	#s = id_cliente.pedido_set.all().aggregate(Sum())
    #----
    
	order_count = pedidos.count()

	myFilter = OrderFilter(request.GET, queryset=pedidos)
	pedidos = myFilter.qs

	context = {'cliente': id_cliente,'pedidos':pedidos, 'order_count':order_count,'myFilter':myFilter}

	return render(request, 'accounts/cliente.html',context)


@login_required(login_url='logar')
@allowed_users(allowed_roles=['admin'])
def fazer_pedido(request, pk):
	OrderFormSet = inlineformset_factory(Cliente, Pedido, fields=('product', 'status'), extra=10 )
	cliente = Cliente.objects.get(id=pk)
	formset = OrderFormSet(queryset=Pedido.objects.none(),instance=cliente)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=cliente)
		if formset.is_valid():
			formset.save()
			return redirect('/')
		else:
			print("erro")

	context = {'formset':formset}
	return render(request, 'accounts/pedido_form.html', context)


@login_required(login_url='logar')
@allowed_users(allowed_roles=['admin'])
def atualizar_pedido(request, id):

	meu_pedido = Pedido.objects.get(id=id)
	form = OrderForm(instance=meu_pedido)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=meu_pedido)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/form_atualizar.html', context)


@login_required(login_url='logar')
@allowed_users(allowed_roles=['admin'])
def remover_pedido(request, id):
	id_pedido = Pedido.objects.get(id=id)
	if request.method == "POST":
		id_pedido.delete()
		return redirect('/')

	context = {'item':id_pedido}
	return render(request, 'accounts/delete.html', context)

