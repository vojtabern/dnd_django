from django.contrib import admin

from .models import *

admin.site.register(Player)
admin.site.register(Level)
admin.site.register(Weapons)
admin.site.register(Class)
admin.site.register(Skills)
admin.site.register(Character)
admin.site.register(Class_has_Skills)