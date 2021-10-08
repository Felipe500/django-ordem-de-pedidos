from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

class OrderForm(ModelForm):
	class Meta:
		model = Pedido
		fields = '__all__'
		

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class ClienteForm(ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Cliente
		fields = '__all__'
		exclude = ['user']

