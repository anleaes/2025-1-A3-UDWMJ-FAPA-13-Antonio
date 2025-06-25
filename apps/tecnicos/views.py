from django.shortcuts import render, redirect, get_object_or_404
from .forms import TecnicoForm
from .models import Tecnico

# Create your views here.

def add_tecnico(request):
    template_name = 'tecnicos/add_tecnico.html'
    context = {}
    if request.method == 'POST':
        form = TecnicoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('tecnicos:list_tecnicos')
    form = TecnicoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tecnicos(request):
    template_name = 'tecnicos/list_tecnicos.html'
    tecnicos = Tecnico.objects.filter()
    context = {
        'tecnicos': tecnicos
    }
    return render(request, template_name, context)

def edit_tecnico(request, id_tecnico):
    template_name = 'tecnicos/add_tecnico.html'
    context ={}
    tecnico = get_object_or_404(Tecnico, id=id_tecnico)
    if request.method == 'POST':
        form = TecnicoForm(request.POST, request.FILES,  instance=tecnico)
        if form.is_valid():
            form.save()
            return redirect('tecnicos:list_tecnicos')
    form = TecnicoForm(instance=tecnico)
    context['form'] = form
    return render(request, template_name, context)

def delete_tecnico(request, id_tecnico):
    tecnico = Tecnico.objects.get(id=id_tecnico)
    tecnico.delete()
    return redirect('tecnicos:list_tecnicos')
