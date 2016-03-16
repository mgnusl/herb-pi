from plants.moisture import *
from plants.valve import *
from plants.models import *


def maybe_water_plant():
    plant = PlantInstance.objects.latest()
    moisture_level = get_moisture(plant.pin_number, plant.sensor_offset_max, plant.sensor_offset_min)
    if moisture_level < LEVELS[plant.plant_type.ideal_humidity]:
        open_valve(plant.pin_number, 1)
        WateringLog.objects.create(num_seconds_open=1)
        MoistureLog.objects.create(moisture_level=moisture_level)
