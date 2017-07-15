from django.contrib import admin

# Register your models here.
from .models import Hardware, Types, Hard_Model, Region, Toch_dost

class RegionInline(admin.StackedInline):
    model = Region


class Toch_dostAdmin(admin.ModelAdmin):
    fields = ['region', 'name']
    list_display = ['region', 'name']
    list_filter = ['region', 'name']
    search_fields = ['name']

# admin.site.register(Toch_dost, Toch_dostAdmin)
admin.site.register(Toch_dost, Toch_dostAdmin)
admin.site.register(Region)