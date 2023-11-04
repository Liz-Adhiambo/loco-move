from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportModelAdmin


admin.site.register(Driver)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(MoveRequest)
admin.site.register(Vehicle)
admin.site.register(Mover)

@admin.register(ClothingLink)
class TimeTrackerLog(ImportExportModelAdmin):
    list_display=("seller_number","price")

