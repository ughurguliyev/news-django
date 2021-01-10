from django.db import models 

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    surname = models.CharField(max_length=100, verbose_name='Surname')
    email = models.EmailField(unique=True, verbose_name='Email')
    username = models.CharField(max_length=100, verbose_name='Username', unique=True)
    bio = models.TextField(verbose_name="Bio", null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    profile_img = models.ImageField(upload_to='users/', null=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    def __str__(self):
        return self.username