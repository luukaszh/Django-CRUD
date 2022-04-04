from django.db import models

class Bee(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return self.name

