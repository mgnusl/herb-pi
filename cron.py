from plants.moisture import *
from plants.models import MoistureLog


def get_moisture_cron():
    MoistureLog.objects.create(get_moisture(0, 140, 1023))

