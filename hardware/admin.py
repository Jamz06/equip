from django.contrib import admin

# Register your models here.
from .models import Ustr, Types, Hard_Model, Region, Toch_dost, Manufacturer

class Ustr_Inline(admin.TabularInline):
    model = Ustr
    extra = 1
    


class Toch_dostAdmin(admin.ModelAdmin):
    fields = ['region', 'name']
    list_display = ['region', 'name']
    list_filter = ['region', 'name']
    search_fields = ['name']
    inlines = [Ustr_Inline]

class Hard_Model_Inline(admin.StackedInline):
    model = Hard_Model
    extra = 5

class ManufacturerAdmin(admin.ModelAdmin):
    inlines = [Hard_Model_Inline]

class UstrAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'toch_dost', 'ip',]
    list_editable = ['toch_dost', 'ip',]

# admin.site.register(Toch_dost, Toch_dostAdmin)
admin.site.register(Toch_dost, Toch_dostAdmin)

admin.site.register(Region)
admin.site.register(Ustr, UstrAdmin)
admin.site.register(Hard_Model)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Types)

