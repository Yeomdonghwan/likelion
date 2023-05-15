from django.contrib import admin
from .models import Post, Comment, FreePost, FreeComment, Tag, Category, Blog

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Blog)
# admin.site.register(FreePost)
# admin.site.register(FreeComment)