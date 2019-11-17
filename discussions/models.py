from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL


class Discussions(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    added_date = models.DateTimeField()
    text = models.CharField(max_length=80)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Discussions"
