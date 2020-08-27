from django.db import models

# Create your models here.

class Story(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural='Stories'