from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    departamento = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "autores"

    def __str__(self):
        return str(self.nombre)


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    titulo_recurso = models.CharField(max_length=500)
    departamento = models.CharField(max_length=200, blank=True)
    tomo = models.CharField(max_length=50, blank=True)
    folio = models.CharField(max_length=50, blank=True)
    tipo_publicacion = models.CharField(max_length=50)
    grupo = models.CharField(max_length=50)
    lugar_pub = models.CharField("Lugar de Publicación", max_length=255)
    issn = models.CharField(max_length=20, blank=True)
    e_issn = models.CharField(max_length=20, blank=True)
    isbn = models.CharField(max_length=20, blank=True)
    cdrom_dvd = models.BooleanField(default=False)
    base_de_datos = models.BooleanField(default=False)
    url = models.CharField(blank=True)
    tipo_recurso = models.CharField(max_length=50)
    fecha = models.DateField(editable=True)
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name="profesores", blank=True
    )

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
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name="tutorias", blank=True
    )

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
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name="bibliografias", blank=True
    )

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"

    def __str__(self):
        return str(self.nombre)
