from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL


class Preferences(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, unique=True,
                             on_delete=models.CASCADE)
    tech = models.TextField(null=True)

    def __str__(self):
        return str(self.user)
