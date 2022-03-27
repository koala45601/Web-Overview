from django.db import models

# Create your models here.

class contract(models.Model):
    title = models.CharField(max_length=250)
    email = models.CharField(max_length=255)
    comment = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.title +self.email+self.comment
