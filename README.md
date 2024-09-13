Documentação do Projeto de Gerenciamento de Tarefas

Índice
Introdução
Configuração do Projeto
Estrutura do Projeto
Descrição das Funcionalidades
Modelos de Dados
Formulários
Views (Funções de Visualização)
URLs
Frontend
Testes
Considerações Finais

1. Introdução
Este projeto é uma aplicação web de gerenciamento de tarefas que permite aos usuários criar, editar, concluir, adiar e excluir tarefas. Ele inclui autenticação de usuários, permitindo que cada um gerencie suas próprias tarefas de forma privada.

Funcionalidades Principais:
Autenticação de usuários (login, registro e logout).
Gerenciamento de tarefas (criação, edição, exclusão).
Listagem de tarefas por status (pendente, concluído, adiado).
Interface para registrar e visualizar usuários.

2. Configuração do Projeto
Pré-requisitos:
Python 3.x
Django 3.x ou superior
Banco de dados (SQLite por padrão)
Passos para Configuração:
Clone o repositório:

git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETÓRIO>

Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows

Instale as dependências:

pip install -r requirements.txt

Execute as migrações do banco de dados:


python manage.py migrate

Inicie o servidor:
python manage.py runserver

3. Estrutura do Projeto
A estrutura básica dos arquivos do projeto Django é a seguinte:

tarefas/

├── admin.py               # Registra o modelo no admin do Django

├── apps.py                # Configurações do app

├── forms.py               # Formulários personalizados

├── models.py              # Modelos de dados (Tarefa, Usuários)

├── urls.py                # Mapeamento de URLs

├── views.py               # Funções de visualização (Views)


4. Descrição das Funcionalidades
Funcionalidades Principais:
Autenticação de Usuário:

Registro de novos usuários (register).
Login e logout (login_view, logout_view).
Gerenciamento de Tarefas:

Listar tarefas pendentes: tarefas_pendentes_list.
Criar novas tarefas: Formulário AdicionarTarefa.
Concluir tarefas: concluir_tarefa.
Adiar tarefas: adiar_tarefa.
Editar tarefas: editar_tarefa.
Excluir tarefas: excluir_tarefa.
Categorias e Status:

As tarefas podem ter três categorias: "Urgente", "Importante" e "Precisa ser feito".
Os status de uma tarefa são "Pendente", "Concluído" e "Adiado".
5. Modelos de Dados (Models)

Tarefa

class Tarefa(models.Model):
    descricao = models.CharField(max_length=400)
    criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=25, choices=OPCOES_CATEGORIA)
    status = models.CharField(max_length=25, choices=OPCOES_STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

Campos:
descricao: Texto da tarefa.
criacao: Data de criação da tarefa.
categoria: Categoria da tarefa (Urgente, Importante, etc.).
status: Estado da tarefa (Pendente, Concluído, Adiado).
user: Referência ao usuário que criou a tarefa.
Usuarios


class Usuarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)


6. Formulários (Forms)
AdicionarTarefa (Formulário de Criação de Tarefas):


class AdicionarTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('descricao', 'categoria')
EditarTarefaForm (Formulário de Edição de Tarefas):


class EditarTarefaForm(forms.Form):
    tarefa = forms.CharField(max_length=400)
    categoria = forms.ChoiceField(choices=OPCOES_CATEGORIA)


7. Views (Funções de Visualização)
Exemplo de Função: tarefas_pendentes_list
Exibe as tarefas pendentes do usuário logado.

@login_required
def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefa.objects.filter(user=request.user, status='pendente')
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.user = request.user
            tarefa.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = AdicionarTarefa()
    return render(request, 'tarefas/tarefas_pendentes.html', {'tarefas_pendentes': tarefas_pendentes, 'form': form})


8. URLs
O arquivo urls.py define as rotas da aplicação. Aqui estão as principais:

urlpatterns = [
    path('', views.tarefas_pendentes_list, name='tarefas_pendentes_list'),
    path('<int:tarefa_id>/concluir/', views.concluir_tarefa, name ='concluir_tarefa'),
    # Outras rotas omitidas
]

9. Frontend
Os templates utilizados estão no diretório templates/, que renderizam as informações e formulários definidos nas views. Aqui estão alguns exemplos de templates que você pode adicionar à documentação:

tarefas/tarefas_pendentes.html: Lista as tarefas pendentes do usuário.
tarefas/editar_tarefa.html: Formulário para edição de tarefa.

10. Testes
A aplicação pode incluir testes no arquivo tests.py para garantir que as funcionalidades estão funcionando corretamente. Exemplo básico de um teste unitário:

from django.test import TestCase
from .models import Tarefa
from django.contrib.auth.models import User

class TarefaModelTest(TestCase):
    def test_tarefa_str(self):
        user = User.objects.create(username='testuser')
        tarefa = Tarefa.objects.create(descricao='Testar tarefa', user=user)
        self.assertEqual(str(tarefa), 'Testar tarefa')



