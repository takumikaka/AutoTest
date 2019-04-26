from django.db import models
from product.models import Product

# Create your models here.

class Bug(models.Model):
    Product = models.ForeignKey("product.Product", on_delete = models.CASCADE, null = True)
    bugname = models.CharField("Bug_Name", max_length = 64)
    bugdetail = models.CharField("Detail", max_length = 200)
    BUG_STATUS = (("Activate", "Activate"), ("Resolved", "Resolved"), ("Closed", "Closed"))
    bugstatus = models.CharField(verbose_name = "Solution_State", choices = BUG_STATUS, default = "Activate", max_length = 200, null = True)
    BUG_LEVEL = (("1", "1"), ("2", "2"), ("3", "3"))
    buglevel = models.CharField(verbose_name = "Bug_Level", choices = BUG_LEVEL, default = "3", max_length = 200, null = True)
    bugcreater = models.CharField("Creater", max_length = 200)
    bugassign = models.CharField("Assign", max_length = 200)
    create_time = models.DateTimeField("Create_Time", auto_now = True)

    class Meta:
        verbose_name = "Bug_Manage"
        verbose_name_plural = "Bug_Manage"

    def __str__(self):
        return self.bugname
