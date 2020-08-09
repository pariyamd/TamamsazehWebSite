
from django.db import models
from tamamsazeh.models import ProjectImage
GENRE = (
    ('1', 'Oil, Gas and Petrochemical'),
    ('2', 'Educational and Cultural Structures'),
    ('3', 'Steal Structures and Bridges'),
    ('4', 'Industrial and Civil Structure'),
    ('5', 'Mass production'),
    ('6', 'Road construction'),
    ('7', 'Others')
)


class BlogFa(models.Model):
    name = models.CharField(max_length=200, blank=True)
    date = models.DateField(blank=True, null=True)
    pdf = models.FileField(blank=True, null=True, upload_to="articles/")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ArticleFa(BlogFa):
    author = models.CharField(max_length=100, blank=True, default='unknown', null=True)


class PostFa(BlogFa):
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)


class ProjectFa(models.Model):
    Album = models.ManyToManyField(ProjectImage, blank=True)
    Title = models.CharField(max_length=200)
    info = models.TextField(blank=True)
    genre = models.CharField(max_length=2, choices=GENRE, default='7')
    isImportant = models.BooleanField(blank=True)

    def __str__(self):
        return self.Title
