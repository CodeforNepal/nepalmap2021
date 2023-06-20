from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(default='enter content here...', verbose_name='content')
    created_on = models.DateTimeField(auto_created=True)
    last_updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
