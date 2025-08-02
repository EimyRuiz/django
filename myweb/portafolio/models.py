from django.db import models

# Create your models here.
class Proyecto(models.Model):
    #variable para el modelo (tabla)
    titulo = models.CharField(max_length=100)
    #titulo con longitud maxima tipo char
    descripcion = models.TextField()
    #descriciop text
    fecha = models.DateField()
    #date fechas
    url = models.URLField(blank=True)
    #para que abra en una nueva pag

#con esto vamos a mostrar/imprimir el titulo otorgado al modelo.
def __str__(self):
        return self.titulo

NIVELES = [
      ('Basico', 'Basico'),
      ('Intermedio', 'Intermedio'),
      ('Avanzado', 'Avanzado'),
]

class Habilidad(models.Model):
      nombre = models.CharField(max_length=100) #Campo de texto corto
      nivel = models.TextField(max_length=20, choices=NIVELES)

      def __str__(self): 
            return f"{self.nombre}, {self.nivel}"