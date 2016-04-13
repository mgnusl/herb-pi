from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from plants.models import Plant, MoistureLog, WateringLog, PlantInstance
from django.shortcuts import render, redirect, get_object_or_404
from plants.serializers import *
from plant_type_form import PlantTypeForm
from plant_instance_form import PlantInstanceForm
from django.contrib import messages
from moisture import *


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

def new_plant(request, id=None):
    if request.method == 'POST':
        form = PlantTypeForm(data=request.POST)
        if form.is_valid():
            if id is not None:
                instance = Plant.objects.get(id=id)
            else:
                instance = Plant()
            instance.name = form.cleaned_data['name']
            instance.ideal_humidity = form.cleaned_data['ideal_humidity']
            instance.sun_preference = form.cleaned_data['sun_preference']
            instance.shade_tolerance = form.cleaned_data['shade_tolerance']
            instance.fertilizing_interval = form.cleaned_data['fertilizing_interval']
            instance.save()
            messages.success(request, 'Plant type saved')
            return redirect('plants/index')
    if id is not None:
        form = PlantTypeForm(instance=Plant.objects.get(id=id))
    else:
        form = PlantTypeForm()
    context = {'form': form, 'id': id}
    return render(request, 'plants/new.html', context)

def delete_plant(request, id):
    plant = Plant.objects.get(id=id)
    plant.delete()
    messages.success(request, 'Plant type deleted')
    return redirect('plants/index')

def plant_instances_index(request):
    context = {'instances': PlantInstance.objects.all()}
    return render(request, 'instances/index.html', context)


def new_plant_instance(request, id=None):
    if request.method == 'POST':
        form = PlantInstanceForm(data=request.POST)
        if form.is_valid():
            if id is not None:
                instance = PlantInstance.objects.get(id=id)
            else:
                instance = PlantInstance()
            instance.plant_type = form.cleaned_data['plant_type']
            instance.pin_number = form.cleaned_data['pin_number']
            instance.save()
            messages.success(request, 'Instance saved')
            return redirect('instances/index')
    if id is not None:
        form = PlantInstanceForm(instance=PlantInstance.objects.get(id=id))
    else:
        form = PlantInstanceForm()
    context = {'form': form, 'id': id}
    return render(request, 'instances/new.html', context)

def delete_plant_instance(request, id):
    plant_instance = PlantInstance.objects.get(id=id)
    plant_instance.delete()
    messages.success(request, 'Plant deleted')
    return redirect('instances/index')


def single_plant_instance(request, pk):
    context = get_object_or_404(PlantInstance, pk=pk)
    moisture_logs = MoistureLog.objects.filter(plant_instance=pk)

    moisture_log_levels = []
    moisture_log_dates = []
    for log_item in moisture_logs:
        moisture_log_dates.append(log_item.date.strftime("%B %d, %Y %H:%M"))
        moisture_log_levels.append(log_item.moisture_level)

    return render(request, 'instances/single_instance.html', {'instance': context, 'moisture_log_levels': moisture_log_levels,
                                                              'moisture_log_dates': moisture_log_dates})

def calibrate_sensor(request, plant_instance_id):
    plant_instance = PlantInstance.objects.get(id=plant_instance_id)
    minmax = request.GET.get('minmax')
    if minmax is not None:
        print minmax
        if minmax == 'min':
            try:
                plant_instance.sensor_offset_min = read_adc(plant_instance.pin_number)
                plant_instance.save()
                messages.success(request, 'Sensor minimum calibrated')
            except Exception as e:
                messages.error(request, 'Unable to get sensor input')
        elif minmax == 'max':
            try:
                plant_instance.sensor_offset_max = read_adc(plant_instance.pin_number)
                plant_instance.save()
                messages.success(request, 'Sensor maximum calibrated')
            except Exception as e:
                messages.error(request, 'Unable to get sensor input')
    context  = {'plant_instance': plant_instance}
    return render(request, 'instances/calibrate.html', context)
