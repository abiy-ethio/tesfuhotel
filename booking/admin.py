from django.contrib import admin
from django.utils import timezone
from django.utils.timezone import now

from .models import Booking

class ItemAdmin(admin.ModelAdmin):
	list_display = ['Name', 'email', 'checkin', 'checkout']

admin.site.register(Booking, ItemAdmin)