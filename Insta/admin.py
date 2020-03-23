from django.contrib import admin

from Insta.models import Post, InstaUser, Comment, Like
# Register your models here.

admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Comment)
admin.site.register(Like)
