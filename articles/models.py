from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    thumb=models.ImageField(default='default.png',blank=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[0:50]+"....."
    def get_absolute_url(self):
            return reverse('like_post', kwargs = {
                'slug': self.slug
            })





class Comment(models.Model):
    post = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
