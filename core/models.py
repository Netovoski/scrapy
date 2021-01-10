from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']


class Movie(models.Model):
    title = models.CharField(max_length=512)
    identifier =models.CharField(max_length=256, null=True)
    url = models.CharField(max_length=1024, null=True)