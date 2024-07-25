from collections import defaultdict
from rest_framework import generics, authentication, permissions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q

from .models import Profesor, avales_tuto, avales_biblio, Autor


from .serializers import (
    ProfesorSerializer,
    TutoSerializer,
    BiblioSerializer,
    AutorSerializer,
)


# aval de publicacion
class ProfesorListCreateView(generics.ListCreateAPIView):
    queryset = Profesor.objects.all().order_by('id') 
    serializer_class = ProfesorSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    


class ProfesorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesor.objects.all().order_by('id') 
    serializer_class = ProfesorSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# aval de tutorias
class TutoListCreateView(generics.ListCreateAPIView):
    queryset = avales_tuto.objects.all().order_by('id') 
    serializer_class = TutoSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class TutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = avales_tuto.objects.all().order_by('id') 
    serializer_class = TutoSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# aval de bibliografia
class BiblioListCreateView(generics.ListCreateAPIView):
    queryset = avales_biblio.objects.all().order_by('id') 
    serializer_class = BiblioSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class BiblioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = avales_biblio.objects.all().order_by('id') 
    serializer_class = BiblioSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ReporteDepartamentoView(ListAPIView):
    serializer_class = None
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Obtener el departamento desde los kwargs
        departamento_clave = self.kwargs.get("departamento", None)

        if departamento_clave is None:
            raise ValueError("Debe proporcionar un departamento.")

        avales_por_tipo = defaultdict(int)

        modelos_relevantes = [Profesor, avales_tuto, avales_biblio]

        for modelo in modelos_relevantes:
            for obj in modelo.objects.filter(departamento=departamento_clave).order_by('id') :
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
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

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
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

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


class AutoresListAPIView(generics.ListCreateAPIView):
    serializer_class = None
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = (
        Autor.objects.all()
    )  # Puedes personalizar este queryset según sea necesario
    serializer_class = AutorSerializer

    def get_queryset(self):
        # Personaliza tu queryset aquí si es necesario
        return (
            super()
            .get_queryset()
            .filter(
                Q(profesores__isnull=False)
                | Q(tutorias__isnull=False)
                | Q(bibliografias__isnull=False)
            )
        )


class AutorAvalListView(ListAPIView):
    serializer_class = None
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs["id"]

        # Filtramos por el autor usando el campo ForeignKey en los modelos de avales
        profesores = Profesor.objects.filter(autor=id)
        tutores = avales_tuto.objects.filter(autor=id)
        biblitecos = avales_biblio.objects.filter(autor=id)

        # Unimos los resultados en una sola lista
        avales = list(profesores) + list(tutores) + list(biblitecos)
        return avales

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Función para determinar el serializer basado en el tipo de objeto
        def get_serializer(obj):
            if isinstance(obj, Profesor):
                return ProfesorSerializer(obj)
            elif isinstance(obj, avales_tuto):
                return TutoSerializer(obj)
            elif isinstance(obj, avales_biblio):
                return BiblioSerializer(obj)
            else:
                raise ValueError("Tipo de objeto desconocido")

        # Aplicar el serializer adecuado a cada objeto en el conjunto de datos
        serialized_data = []
        for obj in queryset:
            serializer = get_serializer(obj)
            serialized_obj = serializer.to_representation(obj)
            serialized_data.append(serialized_obj)

        return Response(serialized_data)
