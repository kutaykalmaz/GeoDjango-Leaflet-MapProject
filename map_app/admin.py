from django.contrib import admin
from .models import MarkedPlaces
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

@admin.register(MarkedPlaces)
class MarkedPlacesAdmin(LeafletGeoAdmin):

    list_display = ["name", "location"]
    