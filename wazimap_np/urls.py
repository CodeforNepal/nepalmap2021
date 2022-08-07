from django.conf.urls import url
from wazimap.urls import urlpatterns
from blog import BlogEntryView

urlpatterns += [
    url(
        regex="^blog$",
        view=BlogEntryView.as_view()
    ),
]
