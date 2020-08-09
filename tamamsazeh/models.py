from django.db import models
from django import template

GENRE = (
    ('1', 'Oil, Gas and Petrochemical'),
    ('2', 'Educational and Cultural Structures'),
    ('3', 'Steal Structures and Bridges'),
    ('4', 'Industrial and Civil Structure'),
    ('5', 'Mass production'),
    ('6', 'Road construction'),
    ('7', 'Others')
)

register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]


class Blog(models.Model):
    name = models.CharField(max_length=200, blank=True)
    date = models.DateField(blank=True, null=True)
    pdf = models.FileField(blank=True, null=True, upload_to="articles/")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Article(Blog):
    author = models.CharField(max_length=100, blank=True, default='unknown', null=True)


class Post(Blog):
    text = models.CharField(max_length=100000, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)


class ProjectImage(models.Model):
    image = models.ImageField(blank=True)
    image_name = models.CharField(max_length=300, default='image')
    isPromo=models.BooleanField(blank=True)
    def __str__(self):
        return self.image_name


class Project(models.Model):
    Album = models.ManyToManyField(ProjectImage, blank=True)
    Title = models.CharField(max_length=200)
    info = models.TextField(blank=True)
    genre = models.CharField(max_length=2, choices=GENRE, default='7')
    isImportant = models.BooleanField(blank=True)

    def __str__(self):
        return self.Title


# class ImportantProject(models.Model):
#     pic = models.ImageField(blank=False)
#     Title = models.CharField(max_length=200)
#     info = models.TextField(blank=True)