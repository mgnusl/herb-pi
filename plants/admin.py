from django.contrib import admin
from .models import Plant
from .models import MoistureLog

admin.site.register(Plant)
admin.site.register(MoistureLog)

