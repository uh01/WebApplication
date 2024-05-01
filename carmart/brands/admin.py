from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.BrandsModel)

class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('brandName',)}
    list_display = ['brandName', 'slug']

admin.site.register(models.BrandsModel, BrandsAdmin)