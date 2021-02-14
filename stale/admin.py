from django.contrib import admin
# register your models here

from stale.models import *

admin.site.register(Staff)
admin.site.register(Species)
admin.site.register(Animal)
