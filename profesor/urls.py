from django.urls import path
from profesor.views import (
    ProfesorListCreateView,
    ProfesorRetrieveUpdateDestroyView,
    TutoListCreateView,
    TutoRetrieveUpdateDestroyView,
    BiblioListCreateView,
    BiblioRetrieveUpdateDestroyView,
    ReporteDepartamentoView,
    ReporteTotalAvalessPorDepartamentoView,
    ReporteTotalAvalessPorFechaView,
    AutoresListAPIView,
    AutorAvalListView,
)

urlpatterns = [
    # avales de publicacion
    path("profesores/", ProfesorListCreateView.as_view(), name="profesor-list"),
    path(
        "profesores/<int:pk>/",
        ProfesorRetrieveUpdateDestroyView.as_view(),
        name="profesor-detail",
    ),
    # avales de tutorias
    path("avales_tuto/", TutoListCreateView.as_view(), name="avles-tuto-list"),
    path(
        "avales_tuto/<int:pk>/",
        TutoRetrieveUpdateDestroyView.as_view(),
        name="avales-tuto-detail",
    ),
    # avales de tutorias
    path("avales_biblio/", BiblioListCreateView.as_view(), name="avles-biblio-list"),
    path(
        "avales_biblio/<int:pk>/",
        BiblioRetrieveUpdateDestroyView.as_view(),
        name="avales-biblio-detail",
    ),
    # reportes
    path(
        "reporte-departamento/<str:departamento>/",
        ReporteDepartamentoView.as_view(),
        name="reporte_departamento",
    ),
    path(
        "reporte-total-avaless-por-departamento/",
        ReporteTotalAvalessPorDepartamentoView.as_view(),
        name="reporte-total-avaless-por-departamento",
    ),
    path(
        "reporte-total-avaless-por-fecha/",
        ReporteTotalAvalessPorFechaView.as_view(),
        name="reporte-total-avaless-por-fecha",
    ),
    path("autores/", AutoresListAPIView.as_view(), name="api-list-autores"),
    path(
        'avales-profesor/<int:id>/',
        AutorAvalListView.as_view(),
        name="api-avales-profesor",
    ),
]
