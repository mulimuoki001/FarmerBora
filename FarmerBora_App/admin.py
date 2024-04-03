from django.contrib import admin
from .models import CustomUser, Post, Category, Author, Reply, Comment

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Reply)
admin.site.register(Comment)
