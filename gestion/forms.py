from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        widgets = {
            'fecha_nacimiento': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none'
                }
            ),
            'biografia': forms.Textarea(
                attrs={
                    'rows': 3,
                    'class': 'w-full border border-gray-300 rounded-lg p-2 resize-none focus:ring-2 focus:ring-blue-500 focus:outline-none'
                }
            )
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        widgets = {
            'fecha_publicacion': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
