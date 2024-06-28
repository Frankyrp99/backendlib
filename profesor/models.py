from django.db import models


class FormatoLibro(models.TextChoices):
    IMPRESO = "IMPRESO", "Libro Impreso"
    DIGITAL = "DIGITAL", "Libro Digital"
    RIMPRESA = "RIMPRESA", "Revista Impresa"
    RDIGITAL = "DDIGITAL", "Revista Digital"


class TipoPublicacion(models.TextChoices):
    LIBRO = "LIBRO", "Libro"
    CAPITULO = "CAPITULO", "Capítulo"
    EPIGRAFE = "EPIGRAFE", "Epígrafe"
    ARTICULO = "ARTICULO", "Artículo"


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    titulo_recurso = models.CharField(max_length=500)
    departamento = models.CharField(max_length=200, blank=True)
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
    fecha = models.DateField(editable=True)

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"

    def __str__(self):
        return str(self.nombre)


class avales_tuto(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    titulo_recurso = models.CharField(max_length=500)
    departamento = models.CharField(max_length=200, blank=True)
    tomo = models.CharField(max_length=50, blank=True)
    folio = models.CharField(max_length=50, blank=True)
    fecha = models.DateField(editable=True)
    

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"

    def __str__(self):
        return str(self.nombre)


class avales_biblio(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    departamento = models.CharField(max_length=200, blank=True)
    tomo = models.CharField(max_length=50, blank=True)
    folio = models.CharField(max_length=50, blank=True)
    rev_bilio = models.CharField(max_length=100, blank=True)
    niv_act = models.CharField(max_length=100, blank=True)
    total_asient = models.CharField(max_length=100, blank=True)
    fecha = models.DateField(editable=True)
    pag = models.CharField(max_length=50, blank=True)
    fecha = models.DateField(editable=True)
    bd_local = models.BooleanField(default=False)
    cd_rom = models.BooleanField(default=False)
    bd_internet = models.BooleanField(default=False)
    curso_pos_bus = models.BooleanField(default=False)
    busqueda_internet = models.BooleanField(default=False)
    biblio_personal = models.BooleanField(default=False)
    otros = models.BooleanField(default=False)
    no_biblio = models.BooleanField(default=False)

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"

    def __str__(self):
        return str(self.nombre)
