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
    # No usamos un serializer porque estamos retornando un diccionario directamente

    def get_queryset(self):
        departamento = self.kwargs["departamento"]
        profesores_filtrados = Profesor.objects.filter(
            departamento__icontains=departamento
        )
        avales_tuto_filtrados = avales_tuto.objects.filter(
            departamento__icontains=departamento
        )
        avales_biblio_filtrados = avales_biblio.objects.filter(
            departamento__icontains=departamento
        )

        # Combina los resultados en Python
        queryset = (
            list(profesores_filtrados)
            + list(avales_tuto_filtrados)
            + list(avales_biblio_filtrados)
        )
        print(queryset)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Procesar los avales para organizarlos por fecha
        reporte = {}
        for avel in queryset:
            fecha = avel.fecha.strftime("%d-%m-%Y")  # Formatear la fecha como desees
            if fecha not in reporte:
                reporte[fecha] = []
            reporte[fecha].append(
                {
                    "tipo": type(avel).__name__,  # Identificar el tipo de avel
                    "nombre_completo": getattr(
                        avel, "nombre_completo", None
                    ),  # Usar el nombre completo si está disponible
                    "departamento": getattr(avel, "departamento", None),
                    "fecha": fecha,
                }
            )

        return JsonResponse(reporte)


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
