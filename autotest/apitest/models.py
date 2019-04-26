from django.db import models
from product.models import Product

# Create your models here.

class Apitest(models.Model):
    Product = models.ForeignKey("product.Product", on_delete = models.CASCADE, null = True)
    apitestname = models.CharField("Process_Interface_Name", max_length = 64)
    apitestdesc = models.CharField("Description", max_length = 64, null = True)
    apitester = models.CharField("Tester", max_length = 16)
    apitestresult = models.BooleanField("Test_Result")
    create_time = models.DateTimeField("Create_Time", auto_now = True)

    class Meta:
        verbose_name = "Process_Scenario_Interface"
        verbose_name_plural = "Process_Scenario_Interface"

    def __str__(self):
        return self.apitestname

class Apistep(models.Model):
    Apitest = models.ForeignKey("Apitest", on_delete = models.CASCADE, )
    apiname = models.CharField("Interface_name", max_length = 100)
    apiurl = models.CharField("URL_Address", max_length = 200)
    apistep = models.CharField("Test_Procedure", max_length = 100, null = True)
    apiparamvalue = models.CharField("Request_Parameters_and_Values", max_length = 800)
    REQUEST_METHOD = (("get", "get"), ("post", "post"), ("put", "put"), ("delete", "delete"), ("patch", "patch"))
    apimethod = models.CharField(verbose_name = "Request_Method", choices = REQUEST_METHOD, default = "get", max_length = 200, null = True)
    apiresult = models.CharField("Expected_Results", max_length = 200)
    apiresponse = models.CharField("Response_Data", max_length = 5000, null = True)
    apistatus = models.BooleanField("Whether_to_Pass")
    create_time = models.DateTimeField("Create_Time", auto_now = True)

    def __str__(self):
        return self.name
