from django.db import models

# Create your models here.


class Discussions(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=80)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Discussions"
