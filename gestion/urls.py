from django.urls import path
from .views import (
    AutorListView, AutorCreateView, AutorUpdateView, AutorDeleteView,
    LibroListView, LibroCreateView, LibroUpdateView, LibroDeleteView
)

urlpatterns = [
    path('autores/', AutorListView.as_view(), name='lista_autores'),
    path('autores/crear/', AutorCreateView.as_view(), name='crear_autor'),
    path('autores/editar/<int:pk>/', AutorUpdateView.as_view(), name='editar_autor'),
    path('autores/eliminar/<int:pk>/', AutorDeleteView.as_view(), name='eliminar_autor'),

    path('libros/', LibroListView.as_view(), name='lista_libros'),
    path('libros/crear/', LibroCreateView.as_view(), name='crear_libro'),
    path('libros/editar/<int:pk>/', LibroUpdateView.as_view(), name='editar_libro'),
    path('libros/eliminar/<int:pk>/', LibroDeleteView.as_view(), name='eliminar_libro'),
]
