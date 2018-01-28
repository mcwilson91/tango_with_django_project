from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    #Adds categories and urls to Pages admin page
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    # auto generate slugs on admin
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)




