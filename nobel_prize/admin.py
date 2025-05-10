from django.contrib import admin
from .models import NobelPrize

@admin.register(NobelPrize)
class NobelPrizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category', 'country')
    search_fields = ('name', 'category', 'country')