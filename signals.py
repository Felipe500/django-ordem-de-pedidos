from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Cliente

def cliente_profile(sender, instance, created, **kwargs):
	if created:
		if not Group.objects.filter(name='usuario').exists():
			print("criando grupo usuario")
			Group.objects.create(nome='usuario')
		group = Group.objects.get(name='usuario')
		instance.groups.add(group)
		Cliente.objects.create(
			user=instance,
			name=instance.username,
			)
		print('perfil criado com sucesso!')

post_save.connect(cliente_profile, sender=User)
