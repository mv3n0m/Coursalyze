from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL


class User_Data(models.Model):
    user = models.OneToOneField(User, blank=True, null=True,
                                on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    college = models.CharField(max_length=50, null=True)
    qualification = models.CharField(max_length=50, null=True)
    contact = models.IntegerField(null=True)
    preferences = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Users_Data"

    def __str__(self):
        return str(self.username)
