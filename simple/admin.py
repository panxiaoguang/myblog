from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']
#@admin.register(Blog)
#class BlogAdmin(admin.ModelAdmin):
   # list_display=['title','author','content','image','pub','category']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['blog','name','email','content','pub']
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
admin.site.register(Blog, PostAdmin)
