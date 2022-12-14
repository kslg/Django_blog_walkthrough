from django.contrib import admin
from .models import Post, Comment, Appointment, Teachers
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    

@admin.register(Comment)
class CommentAdmin (admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approved_comments']

    def approved_comments (self, request, queryset):
        queryset.update(approved=True)


@admin.register(Appointment)
class AppointmentAdmin (admin.ModelAdmin):

    list_display = (
        'date',
        'time',
        'parent_name',
        'teacher_name',
        'child_name',
        'approved'
    )
    search_fields = ['teacher_name', 'child_name']
    actions = ['approved']
    

    def approved(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):

    list_display = ('teacher_name', 'class_name')
    search_fields = ['teacher_name', 'class_name']