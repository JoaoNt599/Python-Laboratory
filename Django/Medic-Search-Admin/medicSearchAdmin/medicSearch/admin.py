from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role',)
        }),
        ('Extras', {
            'fields': ('specialties', 'addresses')
        }),
    )
    
  
    list_display = ('user', 'specialtiesList', 'addressesList',)
    
    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]

    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]
        
    # Filtro de hierarquia com datas
    date_hierarchy = 'created_at'
    list_filter = ('user__is_active',)
    
    exclude = ('favorites', 'created_at', 'updated_at',)
    readonly_fields = ('user',)
    search_fields = ('user__username',)



admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)