from django.contrib import admin
from .models import Survey, Option, Vote

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status', 'creation_date', 'edit_date')
    ordering = ('-id',)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Option)
admin.site.register(Vote)


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