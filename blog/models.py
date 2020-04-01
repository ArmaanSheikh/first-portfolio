from django.db import models

# Create your models here.
class BlogProject(models.Model):
    title = models.CharField(max_length = 100)
    blog_text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
