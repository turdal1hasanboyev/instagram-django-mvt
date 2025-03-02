from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import User, Post, Like, Comment, Story, Message


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        ('Personal Info', {'fields': ('username', 'email',
         'first_name', 'last_name', 'bio', 'avatar')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Followers', {'fields': ('followers',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        ('Create User', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'caption')
    fieldsets = (
        ('Post Information', {'fields': ('user', 'image', 'caption')}),
        ('Timestamps', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)


admin.site.register(Post, PostAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'post__caption')
    readonly_fields = ('created_at',)


admin.site.register(Like, LikeAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'post__caption', 'text')
    fieldsets = (
        ('Comment Details', {'fields': ('user', 'post', 'text')}),
        ('Timestamps', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)


admin.site.register(Comment, CommentAdmin)


class StoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)
    fieldsets = (
        ('Story Details', {'fields': ('user', 'image')}),
        ('Timestamps', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)


admin.site.register(Story, StoryAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('sender__username', 'receiver__username', 'text')
    fieldsets = (
        ('Message Details', {'fields': ('sender', 'receiver', 'text')}),
        ('Timestamps', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)


admin.site.register(Message, MessageAdmin)
