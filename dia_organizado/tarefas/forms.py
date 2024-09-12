from django import forms
from .models import Tarefa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AdicionarTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('descricao', 'categoria')

class EditarTarefaForm(forms.Form):
    OPCOES_CATEGORIA = (
        ('urgente','Urgente'),
        ('importante','Importante'),
        ('precisa ser feito','Precisa ser feito'),
    )

    tarefa = forms.CharField(max_length=400)
    categoria = forms.ChoiceField(choices=OPCOES_CATEGORIA)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nome de usuário',
            'password1': 'Senha',
            'password2': 'Confirmação da senha',
        }
        help_texts = {
            'username': '',
            'password1': (
                'Sua senha deve conter pelo menos 8 caracteres. '
                'Sua senha não pode ser totalmente numérica.'
            ),
            'password2': '',
        }
        error_messages = {
            'password_mismatch': 'As senhas não correspondem.',
        }
