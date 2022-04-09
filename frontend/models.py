from django.db import models
from django.utils import timezone
from PIL import Image
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


# MY PROJECT
class Project(models.Model):
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)
    project_title = models.CharField(max_length=255)
    slug = models.SlugField()
    project_description = models.TextField()
    project_github_link = models.CharField(max_length=255)
    project_live_link = models.CharField(max_length=255, null=True, blank=True)
    project_image = models.ImageField(default='coming_soon.png.png', upload_to='project_pics')  # pip install Pillow
    project_demo_video = EmbedVideoField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_title

    def save(self):
        super().save()
        img = Image.open(self.project_image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.project_image.path)


# Feature Project (Upcoming Project)
class ProjectInMind(models.Model):
    project_title = models.CharField(max_length=255)
    project_description = models.TextField()
    project_image = models.ImageField(default='coming_soon.png', upload_to='project_in_mind_pics')  # pip
    # install Pillow
    project_demo_video = EmbedVideoField()
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Project In Mind"

    def __str__(self):
        return self.project_title

    def save(self):
        super().save()
        img = Image.open(self.project_image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.project_image.path)


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    reply = models.BooleanField(default=False)

    def __str__(self):
        return self.email
