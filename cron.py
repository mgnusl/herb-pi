from plants.moisture import *
from plants.valve import *
from plants.models import *

NUM_SECONDS_OPEN = 1


def maybe_water_plant():
    for plant in PlantInstance.objects.all():
        moisture_level = get_moisture(plant.pin_number, plant.sensor_offset_max, plant.sensor_offset_min)
        MoistureLog.objects.create(moisture_level=moisture_level, plant_instance=plant)
        if moisture_level < LEVELS[plant.plant_type.ideal_humidity]:
            open_valve(plant.pin_number, NUM_SECONDS_OPEN)
            WateringLog.objects.create(num_seconds_open=NUM_SECONDS_OPEN, plant_instance=plant)
