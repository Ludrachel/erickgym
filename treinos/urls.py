from django.urls import path
from treinos import views

urlpatterns = [
    path("treinos", views.get_exercicios_or_criar_exercicio),
    path("treinos/<int:pk>", views.obter_atualizar_apagar)
]