from django.db import models
from product.models import Product

# Create your models here.

class Webcase(models.Model):
    Product = models.ForeignKey("product.Product", on_delete = models.CASCADE, null = True)
    webcasename = models.CharField("Case_Name", max_length = 200)
    webtestresult = models.BooleanField("Test_Result")
    webtester = models.CharField("Tester", max_length = 16)
    create_time = models.DateTimeField("Create_Time", auto_now = True)

    class Meta:
        verbose_name = "Web_Test_Case"
        verbose_name_plural = "Web_Test_Case"

    def __str__(self):
        return self.webcasename

class Webcasestep(models.Model):
    Webcase = models.ForeignKey(Webcase, on_delete = models.CASCADE)
    webcasename = models.CharField("Case_Name", max_length = 200)
    webteststep = models.CharField("Test_Step", max_length = 200)
    webtestobjname = models.CharField("Object_name", max_length = 200)
    webfindmethod = models.CharField("Find_Method", max_length = 200)
    webevelment = models.CharField("Evelment", max_length = 800)
    weboptmethod = models.CharField("Operate_Method", max_length = 200)
    webtestdata = models.CharField("Test_Data", max_length = 200, null = True)
    webassertdata = models.CharField("Assert_Data", max_length = 200)
    webtestresult = models.BooleanField("Test_Result")
    create_time = models.DateTimeField("Create_Time", auto_now = True)

    def __str__(self):
        return self.webcasename
