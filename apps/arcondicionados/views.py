from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArcondicionadoForm
from .models import Arcondicionado

# Create your views here.

def add_arcondicionado(request):
    template_name = 'arcondicionados/add_arcondicionado.html'
    context = {}
    if request.method == 'POST':
        form = ArcondicionadoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('principais:principal')
    form = ArcondicionadoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_arcondicionados(request):
    template_name = 'arcondicionados/list_arcondicionados.html'
    arcondicionados = Arcondicionado.objects.filter()
    context = {
        'arcondicionados': arcondicionados
    }
    return render(request, template_name, context)


def edit_arcondicionado(request, id_arcondicionado):
    template_name = 'arcondicionados/add_arcondicionado.html'
    context ={}
    arcondicionado = get_object_or_404(Arcondicionado, id=id_arcondicionado)
    if request.method == 'POST':
        form = ArcondicionadoForm(request.POST, instance=arcondicionado)
        if form.is_valid():
            form.save()
            return redirect('arcondicionados:list_arcondicionados')
    form = ArcondicionadoForm(instance=arcondicionado)
    context['form'] = form
    return render(request, template_name, context)