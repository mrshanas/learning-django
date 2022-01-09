from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    """Allow users to post pictures"""
    title = models.CharField(max_length=200,blank=True,null=True)

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,related_name='post_created',on_delete=models.CASCADE)

    slug = models.SlugField(max_length=500,blank=True)

    caption = models.TextField(blank=True,null=True)

    image = models.ImageField(upload_to='posts/%Y/%m/%d')

    created = models.DateTimeField(auto_now_add=True)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='post_liked',blank=True)

    def get_absolute_url(self):
        return reverse("posts:post_detail", args=[self.id,self.slug])
    
    class Meta:
        ordering = ['-created',]

    def __str__(self):
        return f"{self.title} by {self.user}"

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)