from django.contrib import admin

from . models import Brand
from . models import PhoneModel
from . models import Review

# Register your models here.

admin.site.register(Brand)
admin.site.register(PhoneModel)
admin.site.register(Review)
