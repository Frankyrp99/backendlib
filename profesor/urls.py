from django.urls import path
from profesor.views import (
    ProfesorListCreateView, ProfesorRetrieveUpdateDestroyView,

)

urlpatterns = [
    path('profesores/', ProfesorListCreateView.as_view(), name='profesor-list'),
    path('profesores/<int:pk>/',
         ProfesorRetrieveUpdateDestroyView.as_view(), name='profesor-detail'),
    
]
