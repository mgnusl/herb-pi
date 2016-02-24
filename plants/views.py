from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from plants.models import Plant
from plants.serializers import PlantSerializer


@api_view(['GET', 'POST'])
def plant_list(request, format=None):
    """
    List all plants, or create a new plant
    """
    if request.method == 'GET':
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def plant_detail(request, pk):
    """
    Retrieve, update or delete single plant
    """
    try:
        plant = Plant.objects.get(pk=pk)
    except Plant.DoesNotExist:
        return Reponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlantSerializer(plant)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlantSerializer(plant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Reponse(serializer.data)
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        plant.delete()
        return Reponse(status=stauts.HTTP_204_NO_CONTENT)        