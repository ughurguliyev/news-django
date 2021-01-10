from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField
from .author import Author
from .category import Category
from .comment import Comment

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', unique=True)
    body = RichTextUploadingField()
    cover_img = models.ImageField(verbose_name='Cover image', null=True, upload_to='post/covers')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category, related_name='categories')
    slug = AutoSlugField(populate_from='title', null=True)
    created_at = models.DateTimeField(null=True)
    view_count = models.PositiveIntegerField(default=0, verbose_name="View count", null=True)
    trending_now = models.BooleanField(default=False, null=True)

    comments = models.ManyToManyField(Comment, related_name='comments', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail-page', args=[self.slug])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    