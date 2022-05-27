from django.db import models

# Create your models here.

class Changos(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dni = models.IntegerField()
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    Vivo = models.BooleanField(default=True)
    Observaciones = models.CharField(max_length=200, blank=True, null=True)