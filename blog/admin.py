from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
# from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)