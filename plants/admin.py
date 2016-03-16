from django.contrib import admin
from .models import *

admin.site.register(Plant)
admin.site.register(MoistureLog)
admin.site.register(WateringLog)
admin.site.register(PlantInstance)