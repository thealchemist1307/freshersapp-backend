from django.db import models


class config(models.Model):
       encoding=models.CharField(max_length=200,blank=False, default=''),
       sampleRateHertz= models.IntegerField(default=1600)
       languageCode= models.CharField(max_length=200,blank=False, default=''),
       enableWordTimeOffsets= models.BooleanField(default=False)
    
    
    
class audio (models.Model):
    
       file = models.FileField(blank=False, null=False)
       def __str__(self):
        return self.file.name