from django.contrib import admin
from .models import BlogEntry


@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    ordering = ['-last_updated_on']
    prepopulated_fields = {"slug": ("title",)}
