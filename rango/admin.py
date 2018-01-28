from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    #Adds categories and urls to Pages admin page
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)



