from django.contrib import admin
from .models import *


@admin.register(BaseInformationHeader)
class BaseInformationHeaderAdmin(admin.ModelAdmin):
    pass


@admin.register(BaseInformation)
class BaseInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    pass
