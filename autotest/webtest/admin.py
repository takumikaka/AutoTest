from django.contrib import admin
from webtest.models import Webcase, Webcasestep

# Register your models here.

class WebcasestepAdmin(admin.TabularInline):
    list_display = ["webcasename", "webteststep", "webtestobjname", "webfindmethod", "webtestresult", "create_time", "id", "webcase"]
    model = Webcasestep
    extral = 1

class WebcaseAdmin(admin.ModelAdmin):
    list_display = ["webcasename", "webtestresult", "create_time", "id"]
    inlines = [WebcasestepAdmin]

admin.site.register(Webcase, WebcaseAdmin)
