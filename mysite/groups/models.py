from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from accounts.models import User

# Create your models here.


class GroupPostModel(models.Model):
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='img/group/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class RegimentModel(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=200)

    def __str__(self):
        return str(self.name)

class GroupModel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    founder = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(User, related_name='group_members', blank=True)
    regiment = models.ManyToManyField(RegimentModel, blank=True)
    posts = models.ManyToManyField(GroupPostModel, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    @property
    def total_members(self):
        return self.members.count()

    @property
    def total_posts(self):
        return self.posts.counts()

    def get_absolute_url(self):
        return reverse('groups:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name))
        super(GroupModel, self).save(*args, **kwargs)



