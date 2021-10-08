from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Cliente

def cliente_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='cliente')
		instance.groups.add(group)
		Cliente.objects.create(
			user=instance,
			name=instance.username,
			)
		print('perfil criado com sucesso!')

post_save.connect(cliente_profile, sender=User)