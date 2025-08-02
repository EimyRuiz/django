from django.contrib import admin

# Register your models here.
#se puede usar la tecla ctrl + space
#lo recomendable es separarlos con una coma para saber que estamos usando.
from .models import Proyecto  # para importar el modelo

admin.site.register(Proyecto)  # lo registras en el adminc
