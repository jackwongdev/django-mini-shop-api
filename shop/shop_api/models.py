from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length = 25)
    value = models.FloatField(default = 0, blank = False)
    isSecret = models.BooleanField(default = False)

    def __str__(self):
        return self.task
