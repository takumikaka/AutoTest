from django.db import models

# Create your models here.

class Set(models.Model):
    setname = models.CharField("System_Name", max_length = 64)
    setvalue = models.CharField("System_Setting", max_length = 200)

    class Meta:
        verbose_name = "System_Setting"
        verbose_name_plural = "System_Setting"

    def __str__(self):
        return self.setname
