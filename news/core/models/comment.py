from django.db import models


class Comment(models.Model):
    body = models.TextField(verbose_name="Comment message")
    email = models.EmailField(verbose_name="Email")
    commenter = models.CharField(max_length=150 ,verbose_name="Name")
    website = models.CharField(max_length=200, verbose_name="Website")
    comment_added_at = models.DateTimeField(auto_now_add=True, null=True)
    


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.body