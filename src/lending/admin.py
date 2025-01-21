from django.contrib import admin
from .models import *


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    ...


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    ...


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    ...


@admin.register(Country)
class CoachAdmin(admin.ModelAdmin):
    ...