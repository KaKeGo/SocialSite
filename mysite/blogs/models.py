from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from accounts.models import Profile, User

# Create your models here.


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True, default='What u want to write?')
    liked = models.ManyToManyField(User, related_name='post_like', blank=True)
    image = models.ImageField(upload_to='img/posts/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    create_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_on']
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'

    def __str__(self):
        return str(self.author) + str(self.pk)

    @property
    def total_likes(self):
        return self.liked.count()

    def get_absolute_url(self):
        return reverse('blogs:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.author) + ':' + str(self.pk))
        super(Posts, self).save(*args, **kwargs)
