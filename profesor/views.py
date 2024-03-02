from django.shortcuts import render
from rest_framework import generics, authentication, permissions

from .models import Profesor
#from .filters import ProfesorFilter, ArticuloFilter, LibroFilter
from .serializers import ProfesorSerializer

class ProfesorListCreateView(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    #filterset_class = ProfesorFilter
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

class ProfesorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    #filterset_class = ProfesorFilter
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]


