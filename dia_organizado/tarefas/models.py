from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    OPCOES_STATUS = (
        ('concluído', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
    )

    OPCOES_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito'),
    )

    descricao = models.CharField(max_length=400)
    criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=25, choices=OPCOES_CATEGORIA, default='importante')
    status = models.CharField(max_length=25, choices=OPCOES_STATUS, default='pendente')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Campo de usuário adicionado

    def __str__(self):
        return self.descricao

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

