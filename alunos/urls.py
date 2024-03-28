from django.urls import path
from alunos import views

urlpatterns = [
    path("alunos", views.obter_or_criar_aluno),
    path("alunos/<int:pk>", views.obter_atualizar_apagar)
]