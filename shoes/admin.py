from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Categories)
admin.site.register(models.Brand)
admin.site.register(models.Shoes)
admin.site.register(models.SavedShoes)