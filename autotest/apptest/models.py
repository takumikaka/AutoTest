from django.db import models

# Create your models here.

class Appcase(models.Model):
    Product = models.ForeignKey("product.Product", on_delete = models.CASCADE, null = True)
    appcasename = models.CharField("Case_Name", max_length = 200)
    apptestresult = models.BooleanField("Test_Result")
    apptester = models.CharField("Tester", max_length = 16)
    create_time = models.DateTimeField("Create_Time", auto_now = True)

    class Meta:
        verbose_name = "App_TestCase"
        verbose_name_plural = "App_TestCase"

    def __str__(self):
        return self.appcasename

class Appcasestep(models.Model):
    Appcase = models.ForeignKey("Appcase", on_delete = models.CASCADE)
    appteststep = models.CharField("Test_Step", max_length = 200)
    apptestobjname = models.CharField('Test_Object_Name', max_length = 200)
    appfindmethod = models.CharField('Find_Method', max_length = 200)
    appevelement = models.CharField('Evelement', max_length = 800)
    appoptmethod = models.CharField('Operate_Method', max_length = 200)
    apptestdata = models.CharField('Test_Data', max_length = 200, null = True)
    appassertdata = models.CharField('Assert_Data', max_length = 200)
    apptestresult = models.BooleanField('Test_Result')
    create_time = models.DateTimeField('Create_Time', auto_now = True)

    def __str__(self):
        return self.appteststep
