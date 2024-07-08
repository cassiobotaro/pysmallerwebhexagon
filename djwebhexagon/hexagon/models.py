from django.db import models


class Rate(models.Model):
    value = models.FloatField()
    slug = models.SlugField()

    def __str__(self):
        return str(self.slug)
