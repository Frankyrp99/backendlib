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
    nombre = models.CharField("Nombre del profesor", max_length=255)
    apellidos = models.CharField("Apellidos del profesor", max_length=255)
    ci = models.CharField("CI del profesor", max_length=11, validators=[RegexValidator(
        r'^\w{11}$', 'El CI debe tener exactamente 11 caracteres.')], unique=True)
    titulo_recurso = models.CharField("Titulo del Recurso", max_length=255)
    tipo_publicacion = models.CharField("Tipo de la publicación", max_length=255, choices=TipoPublicacion.choices)
    lugar_pub = models.CharField("Lugar de Publicación", max_length=255)
    formato = models.CharField("Formato del Artículo", max_length=255, choices=FormatoLibro.choices)
    issn = models.CharField("ISSN ", max_length=255, unique=True, blank=True)
    e_issn = models.CharField("E-ISSN", max_length=255, unique=True, blank=True)
    isbn = models.CharField("ISBN", max_length=255, blank=True)
    url = models.CharField("Url del Sitio Web", max_length=255, blank=True)
    database = models.BooleanField('base de datos',default=False)
    cd_rom = models.BooleanField('CD-ROM/DVD',default=False)
    tomo = models.CharField("Tomo", max_length=255)
    folio = models.CharField("Folio", max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

