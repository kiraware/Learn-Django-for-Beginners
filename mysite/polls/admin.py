from django.contrib import admin

from .models import Choice, Question

# bentuk Choice tampil di Question Admin
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # ordering model fields

    '''
    fieldsets = [
        # title
        (None,               {'fields' : ['question_text']}),
        ('Date information', {'fields' : ['pub_date']}),
    ]
    '''
    fieldsets = [
        # title
        (None,               {'fields' : ['question_text']}),
        ('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
    ]

    # nempel sama Choice
    inlines = [ChoiceInline]

    # nampilin Question list default=str(model), diganti sama ini
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # nampilin filter di Question list
    list_filter = ['pub_date']

    # kemampuan nyari
    search_fields = ['question_text']

    # berapa list ditampilin per halaman default=100
    # list_per_page

    # Gak tau, mungkin hirarki hari
    # date_hierarchy

admin.site.register(Question, QuestionAdmin)