from django.db import models
#from authentication.models import Profile  # Importa el modelo de perfil si está en otra aplicación

class Encuesta(models.Model):
    #id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True)

class Opcion(models.Model):
    #id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, related_name='opciones', on_delete=models.CASCADE)
    texto_opcion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True)


class Voto(models.Model):
    #id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, related_name='votos', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)


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