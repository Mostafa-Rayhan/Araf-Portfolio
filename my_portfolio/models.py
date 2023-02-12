from django.db import models

# Create your models here.


class All(models.Model):
    category = models.CharField(max_length=150, null=False, blank=False)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='media/all', null=True, blank=True)

    def __str__(self):
        return self.name
