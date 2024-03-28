from rest_framework.views import APIView
from rest_framework.response import Response
from alunos.models import Aluno
from alunos.serializers import AlunoSerializer
from rest_framework.decorators import api_view

# Importa o serializer

@api_view(['GET', 'POST'])
def obter_or_criar_aluno(request):
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data, status=200)
    if request.method == 'POST':
        alunos = AlunoSerializer(data=request.data)
        # If - SE
        if alunos.is_valid():
            alunos.save()
            return Response(alunos.data, status=201)
        else:
            return Response(alunos.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def obter_atualizar_apagar(request, pk):
    alunos = Aluno.objects.get(id=pk)

    if request.method == 'GET':
        selializer = AlunoSerializer(alunos, many=False)
        return Response(selializer.data, status=200)
    
    if request.method == 'PUT':
        selializer = AlunoSerializer(alunos, data=request.data)
        if selializer.is_valid():
            selializer.save()
            return Response(selializer.data)
        else:
            return Response(selializer.errors, status=400)
        
    if request.method == 'DELETE':
        alunos.delete()
        return Response(status=204)
