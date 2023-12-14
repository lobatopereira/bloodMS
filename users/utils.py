from users.models import UserEnfermaria

def c_user_enf(user):
	objects = UserEnfermaria.objects.filter(user=user).first()
	enfermaria = ""
	if objects:
		enfermaria = objects.enfermaria
	return enfermaria