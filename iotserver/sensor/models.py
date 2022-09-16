from django.db import models
# Create your models here.

class TempHumid(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    temperture = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    



