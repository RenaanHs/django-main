from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa, Usuarios
from .forms import AdicionarTarefa, EditarTarefaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Lista de tarefas pendentes (somente para usuários autenticados)
@login_required
def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefa.objects.filter(status='pendente')
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = AdicionarTarefa()
    return render(request, 'tarefas/tarefas_pendentes.html', {
        'tarefas_pendentes': tarefas_pendentes,
        'form': form
    })

# Concluir tarefa
@login_required
def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'concluido'
    tarefa.save()
    return redirect('tarefas_pendentes_list')

# Excluir tarefa
@login_required
def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('tarefas_pendentes_list')

# Adiar tarefa
@login_required
def adiar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'adiado'
    tarefa.save()
    return redirect('tarefas_pendentes_list')

# Editar tarefa
@login_required
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = EditarTarefaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tarefa.descricao = cd['tarefa']
            tarefa.categoria = cd['categoria']
            tarefa.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = EditarTarefaForm(initial={'tarefa': tarefa.descricao, 'categoria': tarefa.categoria})
    return render(request, 'tarefas/editar_tarefa.html', {'tarefa': tarefa, 'form': form})

# Listar tarefas concluídas
@login_required
def tarefas_concluidas_list(request):
    tarefas_concluidas = Tarefa.objects.filter(status='concluido')
    return render(request, 'tarefas/tarefas_concluidas.html', {'tarefas_concluidas': tarefas_concluidas})

# Listar tarefas adiadas
@login_required
def tarefas_adiadas_list(request):
    tarefas_adiadas = Tarefa.objects.filter(status='adiado')
    return render(request, 'tarefas/tarefas_adiadas.html', {'tarefas_adiadas': tarefas_adiadas})

# Mover tarefa para pendentes
@login_required
def mover_para_tarefas(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'pendente'
    tarefa.save()
    return redirect('tarefas_pendentes_list')

# Página de registro
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Página de login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tarefas_pendentes_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Página de logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Listar usuários (somente para autenticados)
@login_required
def usuarios(request):
    usuarios_list = Usuarios.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios_list})
