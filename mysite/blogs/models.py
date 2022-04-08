from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from accounts.models import User

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=1000, default='title')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True, default='What u want to write?')
    liked = models.ManyToManyField(User, related_name='post_like', blank=True)
    image = models.ImageField(upload_to='img/posts/', null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    create_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_on = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['-create_on']
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'

    def __str__(self):
        return str(self.author) + str(self.pk) + str(self.body)

    @property
    def total_likes(self):
        return self.liked.count()


    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.author) + ':' + str(self.id))
        super(Blogs, self).save(*args, **kwargs)
