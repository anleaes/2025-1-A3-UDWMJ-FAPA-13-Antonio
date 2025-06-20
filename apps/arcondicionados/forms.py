from django import forms
from .models import Arcondicionado

class ArcondicionadoForm(forms.ModelForm):

    class Meta:
        model = Arcondicionado
        exclude = ()