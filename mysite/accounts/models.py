from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.template.defaultfilters import slugify

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=35, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=35, unique=True, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    regiment = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='img/avatar.jpg', upload_to='profile/avatars')
    first_name = models.CharField(max_length=30, default='Update name', null=True, blank=True)
    last_name = models.CharField(max_length=30, default='Update last name', null=True, blank=True)
    bio = models.TextField(max_length=1500, default='Write something about your self', null=True, blank=True)
    motto = models.CharField(max_length=100, default='Your motto', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.user.username))
        super(Profile, self).save(*args, **kwargs)
