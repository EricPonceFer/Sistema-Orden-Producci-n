from django.db import models

class Plantilla(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Paso(models.Model):
    plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE, related_name='pasos')
    nombre = models.CharField(max_length=200)
    orden = models.IntegerField()
    tiempo_estimado = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.orden} - {self.nombre}"