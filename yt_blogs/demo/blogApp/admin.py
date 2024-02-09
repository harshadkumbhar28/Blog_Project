from django.contrib import admin
from .models import Tags, Category, Post


# Register your models here.

class TagTubularInline(admin.TabularInline):
    model = Tags


class PostAdmin(admin.ModelAdmin):
    inlines = [TagTubularInline]
    list_display = ['Title', 'Author', 'Date', 'Status', 'Section', 'Main_post', 'Category']
    list_editable = ['Status', 'Section', 'Main_post', 'Category']
    search_fields = ['Title', 'Section']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tags)
