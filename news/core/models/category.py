from django.db import models
from autoslug import AutoSlugField 

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category name')
    slug = AutoSlugField(populate_from='name')
    featured_img = models.ImageField(upload_to='category/', verbose_name='Featured image', null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name