from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Driver)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(MoveRequest)
admin.site.register(Vehicle)
admin.site.register(Mover)
admin.site.register(ClothingLink)

