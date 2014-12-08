from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [('Question Info', {'fields':['question_text']}), ('Date Info', {'fields':['pub_date']})]
    fieldsets = [(None, {'fields':['question_text']}), ('Date Info', {'fields':['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# class ChoiceAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields':['question']}),(None, {'fields':['choice_text','votes']})]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)