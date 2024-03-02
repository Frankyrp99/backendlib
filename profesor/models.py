from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class FormatoLibro(models.TextChoices):
    IMPRESO = 'IMPRESO', 'Libro Impreso'
    DIGITAL = 'DIGITAL', 'Libro Digital'
    RIMPRESA = 'RIMPRESA', 'Revista Impresa'
    RDIGITAL = 'DDIGITAL', 'Revista Digital'


class TipoPublicacion(models.TextChoices):
    LIBRO = 'LIBRO', 'Libro'
    CAPITULO = 'CAPITULO', 'Capítulo'
    EPIGRAFE = 'EPIGRAFE', 'Epígrafe'
    ARTICULO = 'ARTICULO', 'Artículo'


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    titulo_recurso = models.CharField(max_length=200)
    tomo = models.CharField(max_length=50, blank=True)
    folio = models.CharField(max_length=50, blank=True)
    tipo_publicacion = models.CharField(max_length=50)
    lugar_pub = models.CharField("Lugar de Publicación", max_length=255)
    issn = models.CharField(max_length=10, blank=True)
    e_issn = models.CharField(max_length=10, blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    cdrom_dvd = models.BooleanField(default=False)
    base_de_datos = models.BooleanField(default=False)
    url = models.URLField(blank=True)
    tipo_recurso = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

