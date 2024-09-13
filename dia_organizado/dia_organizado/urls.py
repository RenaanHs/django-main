from django.contrib import admin
from django.urls import path, include
from tarefas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', include('tarefas.urls')),
    path('', views.login_view, name='login'),  # Página inicial é o login
    path('usuarios/', views.usuarios, name='usuarios'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')
]
