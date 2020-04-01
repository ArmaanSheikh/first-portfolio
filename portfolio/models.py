from django.db import models
# Create your models here.
class ProtforlioProject(models.Model):
    title = models.CharField(max_length = 100)
    disc  = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = 'portfolio/Images')
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title
