from .models import BlogEntry
from django.views.generic import TemplateView


class BlogEntryView(TemplateView):
    template_name = 'blog/blog_entry.html'

    def get_context_data(self, *args, **kwargs):
        return {
            'blogs': BlogEntry.objects.all(),
        }
