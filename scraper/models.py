from django.db import models

# Create your models here.


class CourseDetail(models.Model):
    title = models.CharField(max_length=50)
    course_url = models.URLField(max_length=200)
    description = models.TextField()
    instructor = models.CharField(max_length=50)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    prerequisites = models.TextField()
    skills_gained = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    enroll_by = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{} => {}'.format(self.title, self.id)


class Search(models.Model):
    search_text = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Searches"
