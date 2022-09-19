from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.models import BlogPage

# from gallery.models import GalleryPage


class HomePage(Page):
    background_img = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    )
    headline = models.CharField(max_length=100, blank=True, null=True)
    sub_headline = models.CharField(max_length=200, blank=True, null=True)
    content_panels = Page.content_panels + [
        ImageChooserPanel("background_img"),
        FieldPanel("headline"),
        FieldPanel("sub_headline"),
    ]

    def blogs(self):
        blogs = BlogPage.objects.live()
        blogs = blogs.order_by("-date")[:6]
        return blogs

    def blog_index(self):
        blogs = BlogPage.objects.live()
        blog = map(lambda b: b.index(), blogs)
        print(blog)
        return blog
