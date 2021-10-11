from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Cliente(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	biografia =  RichTextField(null=True,blank=True )
	img_perfil = models.ImageField( default="profile.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Produto(models.Model):
	CATEGORY = (
			('Interior', 'Interior'),
			('Exterior', 'Exterior'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Pedido(models.Model):
	STATUS = (
			('Pendente', 'Pendente'),
			('Saiu para entrega', 'Saiu para entrega'),
			('Entregue', 'Entregue'),
			)

	customer = models.ForeignKey(Cliente, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Produto, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)
	

	def __str__(self):
		return self.product.name