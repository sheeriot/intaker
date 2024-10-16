from django.contrib import admin
from .models import Rock, Lake

class LakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')

class RockAdmin(admin.ModelAdmin):
    search_fields = ['lake', 'name', 'marker_id']
    list_display = [
        'lake',
        'name', 'marker_id', 'status',
        'latitude', 'longitude',
        'depth', 'size',
        'more_info'
    ]
    list_filter = ['lake']
    ordering = ('lake', 'marker_id', 'name')

admin.site.register(Lake, LakeAdmin)
admin.site.register(Rock, RockAdmin)
