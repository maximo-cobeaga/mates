from django.contrib import admin
from .models import PostModel
# Register your models here.
admin.site.register(PostModel)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    ordering = ['fecha']