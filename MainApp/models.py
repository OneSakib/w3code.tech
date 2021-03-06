from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse_lazy
from django.conf import settings

# Create your models here.
HOST_NAME = settings.HOST_NAME
TUT_TYPES = (
    ('Programming-Language', 'Programming-Language'),
    ('Preparation', 'Preparation'),
    ('Theory-Tutorial', 'Theory-Tutorial'),
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('Javascript', 'Javascript'),
    ('Database-Tutorial', 'Database-Tutorial'),
    ('Web-Technology', 'Web-Technology'),
    ('Microsoft-Office', 'Microsoft-Office'),
    ('Versioning-Control', 'Versioning-Control'),
    ('Web-Hosting', 'Web-Hosting'),
)


class TutList(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TUT_TYPES, default='Python')
    image = models.ImageField(upload_to='tut-icon/')
    link = models.URLField(default=HOST_NAME + "/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tut-Lists'


class TutCommonParent(models.Model):
    title = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title


class TutCommon(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='1')
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now=True)
    content = HTMLField()
    viewcounter = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class LikeCommon(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Likes of {self.user}"


class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Commented by {self.name}'


class Blogs(TutCommon):
    image = models.ImageField(upload_to='blogs/', default='')

    class Meta:
        verbose_name_plural = 'Blogs'

    def get_absolute_url(self):
        return f'{reverse_lazy("w3c:blogdetail", kwargs={"slug": self.slug})}'


class BlogComments(Comments):
    ip_address = models.GenericIPAddressField(default="45.243.82.169")
    post = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='BlogComments')

    class Meta:
        verbose_name_plural = 'BlogComments'


class ArticleBookmark(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='articlebookmark')
    title = models.CharField(max_length=300)
    link = models.URLField()

    class Meta:
        verbose_name_plural = 'User Article Bookmark'

    def __str__(self):
        return self.title


# Like Counter
class BlogsLike(LikeCommon):
    post = models.ForeignKey(Blogs, on_delete=models.CASCADE)


# user account Verification
class EmailVerification(models.Model):
    user = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()

    def __str__(self):
        return self.user.username


# Contact us

class ContactUsModel(Comments):
    class Meta:
        verbose_name_plural = 'Contact US page'


# Profile Image
class ProfileImage(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(default='userprofile/default.jpg', upload_to='userprofile')

    def __str__(self):
        return f"{self.user}' Profile"


class AuthorModel(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='author')
    profession = HTMLField()

    def __str__(self):
        return self.user.username
