from django.db import models
# from authentication.models import Profile  # Import the profile model if it's in another application

class Survey(models.Model):
    # id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

class Option(models.Model):
    # id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

class Vote(models.Model):
    # id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, related_name='votes', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


# ---------------------------------------------------------------




# ---------------------------------------------------------------
# Siempre para cada modificacion y Creando cossas nuevas en DJANGO
# ---------------------------------------------------------------
# Adentro de -> archivo core:

# 1. Genera los archivos de migración para los cambios en BaseDatos:
# (Siempre que agamos un cambio esto se debe que HACER para ACTUALIZAR)
# comando -> [python manage.py makemigrations]

# 2. Aplicar migraciones en el Admin, de todas que trae Django por defecto:
# _ comando -> [python manage.py migrate]

# ---------------------------------------------------------------