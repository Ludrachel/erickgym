from rest_framework.decorators import api_view
from rest_framework.response import Response
from treinos.models import Exercicio
from treinos.serializers import ExercicioSerializer

@api_view(['GET', 'POST'])
def get_exercicios_or_criar_exercicio(request):
    if request.method == 'GET':
        exercicios = Exercicio.objects.all()
        serializer = ExercicioSerializer(exercicios, many=True)
        return Response(serializer.data, status=200)
    if request.method == 'POST':
        exercicio = ExercicioSerializer(data=request.data)
        if exercicio.is_valid():
            exercicio.save()
            return Response(exercicio.data, status=201)
        else:
            return Response(exercicio.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def obter_atualizar_apagar(request, pk):
    exercicio = Exercicio.objects.get(id=pk)

    if request.method == 'GET':
        selializer = ExercicioSerializer(exercicio, many=False)
        return Response(selializer.data, status=200)
    
    if request.method == 'PUT':
        exercicio_serializer = ExercicioSerializer(exercicio, data=request.data)
        if exercicio_serializer.is_valid():
            exercicio_serializer.save()
            return Response(exercicio_serializer.data,status=200)
        else:
            return Response(exercicio_serializer.errors,status=400)
    
    if request.method == 'DELETE':
        exercicio.delete()
        return Response(status=204)