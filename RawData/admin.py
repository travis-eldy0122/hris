from django.contrib import admin
from .models import StaffData, District, School, Position, PositionType


admin.site.register(StaffData)
admin.site.register(District)
admin.site.register(School)
admin.site.register(Position)
admin.site.register(PositionType)