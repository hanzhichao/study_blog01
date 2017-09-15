from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blog.models import Post, Category, BlogComment, User


class BlogUserAdmin(UserAdmin):
    pass


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time')

admin.site.register(Post, BlogAdmin)
admin.site.register(Category)
admin.site.register(BlogComment)
admin.site.register(User, BlogUserAdmin)

