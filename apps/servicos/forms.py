from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['tecnico'].label_from_instance = lambda obj: f"{obj.nome} ({obj.especialidade})"
        if 'arcondicionado' in self.fields:
            self.fields['arcondicionado'].label_from_instance = lambda obj: f"{obj.marca} ({obj.modelo})"
    
    class Meta:
        model = Servico
        exclude = ()