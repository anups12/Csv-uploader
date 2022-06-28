from django.db import models

# Create your models here.
class Csvdata(models.Model):
    name= models.CharField(max_length=100, null=True)
    detected = models.CharField(max_length=100, null=True)
    dateadd = models.DateField()
    image= models.ImageField(default='upload.jpg', null=True)

    def __str__(self):
        return self.name

class UploadCsv(models.Model):
    Fileupload= models.FileField(upload_to='data')

    def __str__(self):
        return str(self.id)

