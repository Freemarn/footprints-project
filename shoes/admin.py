from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px;/>'.format(obj.image.url))
    
    def name_tag(self, obj):
        return format_html(f'<p>{obj.image.name}</p>')

    list_display = ['image_tag', 'name_tag']
    readonly_fields = ['img_preview']

admin.site.register(models.Categories)
admin.site.register(models.Brand)
admin.site.register(models.Shoes, ImageAdmin)
admin.site.register(models.SavedShoes)