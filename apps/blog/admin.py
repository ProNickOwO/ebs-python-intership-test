from django.contrib import admin
from apps.blog.models import Blog, Category, Comment


def make_published(modeladmin, request, queryset):
    queryset.update(enabled=True)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled')
    ordering = ['title']
    actions = [make_published]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    ordering = ['title']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'blog']
    ordering = ['text']


make_published.short_description = "Mark selected stories as published"

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
