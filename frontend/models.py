from django.db import models

# Create your models here.
class videoDB(models.Model):
    videofile = models.FileField(upload_to='videos/')
    Tname = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.title