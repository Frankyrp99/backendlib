from rest_framework import generics
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from collections import defaultdict

from .models import Profesor, avales_tuto, avales_biblio


from .serializers import ProfesorSerializer, TutoSerializer, BiblioSerializer


# aval de publicacion
class ProfesorListCreateView(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer


class ProfesorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer


# aval de tutorias
class TutoListCreateView(generics.ListCreateAPIView):
    queryset = avales_tuto.objects.all()
    serializer_class = TutoSerializer


class TutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = avales_tuto.objects.all()
    serializer_class = TutoSerializer


# aval de bibliografia
class BiblioListCreateView(generics.ListCreateAPIView):
    queryset = avales_biblio.objects.all()
    serializer_class = BiblioSerializer


class BiblioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = avales_biblio.objects.all()
    serializer_class = BiblioSerializer


class ReporteDepartamentoView(ListAPIView):
    serializer_class = None

    def get_queryset(self):
        # Obtener el departamento desde los kwargs
        departamento_clave = self.kwargs.get("departamento", None)
        
        if departamento_clave is None:
            raise ValueError("Debe proporcionar un departamento.")

        avales_por_tipo = defaultdict(int)

        modelos_relevantes = [Profesor, avales_tuto, avales_biblio]

        for modelo in modelos_relevantes:
            for obj in modelo.objects.filter(departamento=departamento_clave):
                if hasattr(obj, "departamento"):
                    avales_por_tipo[obj.__class__.__name__] += 1

        reporte = {
            "total_avales": sum(avales_por_tipo.values()),
            "avales_por_tipo": dict(avales_por_tipo),
        }

        return reporte

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return JsonResponse(queryset, safe=False)

class ReporteTotalAvalessPorDepartamentoView(ListAPIView):
    serializer_class = None

    def get_queryset(self):
        # Conteo inicial de avales por departamento
        avales_por_departamento = defaultdict(int)

        # Iteramos sobre todos los modelos relevantes
        modelos_relevantes = [Profesor, avales_tuto, avales_biblio]
        for modelo in modelos_relevantes:
            for obj in modelo.objects.all():
                if obj.departamento:

                    avales_por_departamento[obj.departamento] += 1

        reporte = dict(avales_por_departamento)

        return reporte

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return JsonResponse(queryset)


class ReporteTotalAvalessPorFechaView(ListAPIView):
    serializer_class = None

    def get_queryset(self):

        avales_por_fecha_completa = defaultdict(lambda: defaultdict(int))

        modelos_relevantes = [Profesor, avales_tuto, avales_biblio]

        for modelo in modelos_relevantes:
            for obj in modelo.objects.all():
                if hasattr(obj, "fecha") and obj.fecha:

                    fecha_formateada = obj.fecha.strftime("%Y-%m-%d")

                    año, mes, dia = fecha_formateada.split("-")

                    clave_fecha = f"{año}"
                    avales_por_fecha_completa[clave_fecha][obj.departamento] += 1

        reporte = {}
        for fecha_completa, departamentos in avales_por_fecha_completa.items():
            total_avales = sum(departamentos.values())
            reporte[fecha_completa] = {
                "fecha": fecha_completa,
                "total": total_avales,
                "departamentos": departamentos,
            }

        return reporte

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return JsonResponse(queryset, safe=False)


class AutoresListAPIView(ListAPIView):
    serializer_class = None  # No necesitamos especificar un serializer_class aquí

    def list(self, request, *args, **kwargs):
        # Inicializar una lista vacía para almacenar los objetos de autor
        autores = []

        # Agregar información de Profesor
        profesores = Profesor.objects.all()
        for profesor in profesores:
            autor_info = {
                "nombre": profesor.nombre,
                "apellidos": profesor.apellidos,
                "departamento": profesor.departamento,
            }
            autores.append(autor_info)

        # Agregar información de avales_tuto
        tutores = avales_tuto.objects.all()
        for tutor in tutores:
            autor_info = {
                "nombre": tutor.nombre,
                "apellidos": tutor.apellidos,
                "departamento": tutor.departamento,
            }
            autores.append(autor_info)

        # Agregar información de avales_biblio
        biblitecos = avales_biblio.objects.all()
        for bibliteco in biblitecos:
            autor_info = {
                "nombre": bibliteco.nombre,
                "apellidos": bibliteco.apellidos,
                "departamento": bibliteco.departamento,
            }
            autores.append(autor_info)

        # Devolver la lista de autores como una respuesta JSON
        return JsonResponse(autores, safe=False)


class AvalProfesorListView(ListAPIView):
    serializer_class = None

    def get_queryset(self):
        nombre = self.request.query_params.get("nombre")
        apellidos = self.request.query_params.get("apellidos")

        profesores = Profesor.objects.filter(
            nombre__icontains=nombre, apellidos__icontains=apellidos
        )
        tutores = avales_tuto.objects.filter(
            nombre__icontains=nombre, apellidos__icontains=apellidos
        )
        biblitecos = avales_biblio.objects.filter(
            nombre__icontains=nombre, apellidos__icontains=apellidos
        )
        avales = list(profesores) + list(tutores) + list(biblitecos)
        return avales

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        avales_dict = [obj.__dict__ for obj in queryset]
        return JsonResponse(avales_dict, safe=False)
