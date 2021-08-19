from django.forms import ModelForm, CharField, TextInput
from cadastro.models import Pessoa

class PessoaForm(ModelForm):
    cpf = CharField(max_length=14, widget= TextInput(attrs={'onkeypress': "$(this).mask('000.000.000-00');", 'onload': "$(this).mask('000.000.000-00');"}))
    class Meta:
        model = Pessoa
        fields = ['cpf', 'nome', 'cnh', 'categoria', 'rntrc', 'e_mail']