from django.contrib import admin

from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('id', 'first_name', )
    search_fields = ('first_name', 'last_name')
    list_filter = ('designation',)

# Register your models here.

admin.site.register(Team, TeamAdmin)