from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from plants.models import Plant, MoistureLog, WateringLog, PlantInstance
from django.shortcuts import render
from plants.serializers import *


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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def plant(request, pk):
    """
    Retrieve, update or delete single plant
    """
    try:
        plant_object = Plant.objects.get(pk=pk)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlantSerializer(plant_object)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlantSerializer(plant_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        plant_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def moisture_sensor_log(request, fk, format=None):
    """
    List log data from moisture sensor for a specific plantinstance (fk)
    """
    if request.method == 'GET':
        moisture_log = MoistureLog.objects.filter(plant_instance=fk)
        serializer = MoistureLogSerializer(moisture_log, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def watering_log(request, fk, format=None):
    """
    List log data from water valve for a specific plantinstance (fk)
    """
    if request.method == 'GET':
        wateringlog = WateringLog.objects.filter(plant_instance=fk)
        serializer = WateringLogSerializer(wateringlog, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def plant_instance(request, pk):
    """
    Retrieve, update or delete a plant instance
    """
    try:
        plantinstance = PlantInstance.objects.get(pk=pk)
    except PlantInstance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlantInstanceSerializer(plantinstance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlantInstanceSerializer(plantinstance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        plantinstance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def plantinstance_list(request, format=None):
    """
    List all plantinstances, or create a new plantinstance
    """
    if request.method == 'GET':
        plant_instances = PlantInstance.objects.all()
        serializer = PlantInstanceSerializer(plant_instances, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlantInstanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def plants_index(request):
    context = {'plants': Plant.objects.all()}
    return render(request, 'plants/index.html', context)
