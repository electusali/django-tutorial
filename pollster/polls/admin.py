from django.contrib import admin

from .models import Question,Choice

admin.site.site_header='Pollster Admin'
admin.site.site_title='Pollster Admin Area'
admin.site.site_index='welcom the pollster admin'

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3
class Questionadmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question_test']}),

    ('Date Infarmation',{'fields':['pub_date'],'classes':['collapse']}),]

    inlines=[ChoiceInline]
admin.site.register(Question,Questionadmin)
    
