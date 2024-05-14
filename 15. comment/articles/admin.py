from django.contrib import admin

from .models import Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    # extra = 0 # untuk ngasih berapa empty comment di admin page, default=3

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)