from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

def inicio(request):
    return render(request, 'gestion/inicio.html')


class AutorListView(ListView):
    model = Autor
    template_name = 'gestion/lista_autores.html'
    context_object_name = 'autores'


class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_form.html'
    success_url = reverse_lazy('lista_autores')


class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_form.html'
    success_url = reverse_lazy('lista_autores')


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'gestion/autor_confirm_delete.html'
    success_url = reverse_lazy('lista_autores')

class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/lista_libros.html'
    context_object_name = 'libros'


class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('lista_libros')


class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('lista_libros')


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'gestion/libro_confirm_delete.html'
    success_url = reverse_lazy('lista_libros')

def lista_autores_func(request):
    autores = Autor.objects.all()
    return render(request, 'gestion/lista_autores_func.html', {'autores': autores})

def crear_autor_func(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores_func')
    else:
        form = AutorForm()
    return render(request, 'gestion/autor_form_func.html', {'form': form})

def actualizar_autor_func(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores_func')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'gestion/autor_form_func.html', {'form': form})

def eliminar_autor_func(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores_func')
    return render(request, 'gestion/autor_confirm_delete_func.html', {'autor': autor})

# --- Libros ---
def lista_libros_func(request):
    libros = Libro.objects.all()
    return render(request, 'gestion/lista_libros_func.html', {'libros': libros})

def crear_libro_func(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros_func')
    else:
        form = LibroForm()
    return render(request, 'gestion/libro_form_func.html', {'form': form})

def actualizar_libro_func(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros_func')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestion/libro_form_func.html', {'form': form})

def eliminar_libro_func(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros_func')
    return render(request, 'gestion/libro_confirm_delete_func.html', {'libro': libro})
