from django.contrib import admin
from . import models

# Car.

class ImageInline(admin.TabularInline):
    model = models.Image
    extra = 3

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model')
    inlines = [ImageInline]


# Details.
@admin.register(models.Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('car',)

# Features.
@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('car',)