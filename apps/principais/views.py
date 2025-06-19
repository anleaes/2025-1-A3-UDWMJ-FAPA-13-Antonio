from django.shortcuts import render

# Create your views here.

def principal(request):
    template_name ='principais/principal.html'
    context = {}
    return render(request, template_name, context)

