from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Category(models.Model):

    NAME = (
        ('Entertainment', 'Entertainment'),
        ('World', 'World'),
        ('Business', 'Business'),
        ('Technology', 'Technology'),
    )

    Name = models.CharField(choices=NAME, max_length=200)

    def __str__(self):
        return self.Name


class Post(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Publish', 'Publish')
    )

    SECTION = (
        ('Popular', 'Popular'),
        ('Recent', 'Recent'),
        ('Editors_Pick', 'Editors_Pick'),
        ('Trending', 'Trending'),
        ('Inspiration', 'Inspiration'),
        ('Latest_Post', 'Latest_Post'),

    )

    Featured_image = models.ImageField(upload_to="Images")
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)
    Content = RichTextField()
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
    Status = models.CharField(choices=STATUS, max_length=100)
    Section = models.CharField(choices=SECTION, max_length=100)
    Main_post = models.BooleanField(default=False)

    def __str__(self):
        return self.Title


def create_slug(instance, new_slug=None):
    slug = slugify(instance.Title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exist = qs.exists()

    if exist:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    pre_save.connect(pre_save_post_receiver, Post)


class Tags(models.Model):
    Name = models.CharField(max_length=100)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
