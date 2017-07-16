from django.contrib import admin

# Register your models here.
from .models import Ustr, Types, Hard_Model, Region, Toch_dost, Manufacturer, Advanced_GW, Connection_type, Provider

admin.AdminSite.site_header = "COCOS EQUIP ADMIN"
admin.AdminSite.site_title = "COCOS EQUIP"
class Ustr_Inline(admin.StackedInline):
    model = Ustr
    extra = 0
    


class Toch_dostAdmin(admin.ModelAdmin):
    fields = ['region', 'name']
    list_display = ['__str__', 'region', 'name']
    list_filter = ['region', 'name']
    search_fields = ['name']
    inlines = [Ustr_Inline]

class Hard_Model_Inline(admin.TabularInline):
    model = Hard_Model
    extra = 0

class ManufacturerAdmin(admin.ModelAdmin):
    inlines = [Hard_Model_Inline]

class Advanced_GWInline(admin.StackedInline):
    model = Advanced_GW
    extra = 0

class Connection_typeInline(admin.TabularInline):
    model = Connection_type
    extra = 0


class UstrAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'toch_dost', 'ip',]
    
    search_fields = ['__str__']
    list_editable = ['toch_dost', 'ip',]
    inlines = [Advanced_GWInline, Connection_typeInline]
    save_as = True
    ''' 
    def check_gw(self):
        if (hard)
        inlines = [Advanced_GWInline]
    fieldsets = [
        ('Общие', {'fields': ('toch_dost', 'model', 'hard_type', 'ip', 'mask', 'login', 'password', 'config') }),
        #('Дополнительные', {'fields': [Advanced_GWInline], 'classes': ['collapse']}),
    ] '''
# admin.site.register(Toch_dost, Toch_dostAdmin)
admin.site.register(Toch_dost, Toch_dostAdmin)

admin.site.register(Region)
admin.site.register(Ustr, UstrAdmin)
admin.site.register(Hard_Model)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Types)

