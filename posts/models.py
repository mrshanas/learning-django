from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    """Allow users to post pictures"""
    title = models.CharField(max_length=200)

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,related_name='post_created',on_delete=models.CASCADE)

    caption = models.TextField(blank=True)

    image = models.ImageField(upload_to='posts/%Y/%m/%d')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created',]

    def __str__(self):
        return f"posts by {self.user} created"