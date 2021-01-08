from django.contrib import admin

from .models import Choice, Logg, Person, Question, User   # noqa: F401


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class LogAdmin(admin.ModelAdmin):
    model = Logg
    list_display = ('path', 'method', 'timestamp')


admin.site.register(Logg, LogAdmin)
admin.site.register(User)
