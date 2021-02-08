from django.contrib import admin

from .models import Human, Interest, Quot, QuoteAuthor


@admin.register(Interest)
class InterestModelAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Human)
class HumanModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'mobile']


@admin.register(Quot)
class QuotesModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


@admin.register(QuoteAuthor)
class AuthorQuotesModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'born_in', 'date_of_birth', 'description']
