from django.contrib import admin

from .models import Human, Interest


@admin.register(Interest)
class InterestModelAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Human)
class HumanModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'mobile']
