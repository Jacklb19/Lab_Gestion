from django.urls import path
from . import views

urlpatterns = [
    # --- CBV Autores ---
    path('autores/', views.AutorListView.as_view(), name='lista_autores'),
    path('autores/nuevo/', views.AutorCreateView.as_view(), name='crear_autor'),
    path('autores/editar/<int:pk>/', views.AutorUpdateView.as_view(), name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.AutorDeleteView.as_view(), name='eliminar_autor'),

    # --- FBV Autores con templates alternativos ---
    path('autores-func/', views.lista_autores_func, name='lista_autores_func'),
    path('autores-func/nuevo/', views.crear_autor_func, name='crear_autor_func'),
    path('autores-func/editar/<int:pk>/', views.actualizar_autor_func, name='actualizar_autor_func'),
    path('autores-func/eliminar/<int:pk>/', views.eliminar_autor_func, name='eliminar_autor_func'),

    # --- CBV Libros ---
    path('libros/', views.LibroListView.as_view(), name='lista_libros'),
    path('libros/nuevo/', views.LibroCreateView.as_view(), name='crear_libro'),
    path('libros/editar/<int:pk>/', views.LibroUpdateView.as_view(), name='editar_libro'),
    path('libros/eliminar/<int:pk>/', views.LibroDeleteView.as_view(), name='eliminar_libro'),

    # --- FBV Libros con templates alternativos ---
    path('libros-func/', views.lista_libros_func, name='lista_libros_func'),
    path('libros-func/nuevo/', views.crear_libro_func, name='crear_libro_func'),
    path('libros-func/editar/<int:pk>/', views.actualizar_libro_func, name='actualizar_libro_func'),
    path('libros-func/eliminar/<int:pk>/', views.eliminar_libro_func, name='eliminar_libro_func'),
]
