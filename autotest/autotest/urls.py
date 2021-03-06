"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apitest import views
from product import proviews
from bug import bugviews
from set import setviews
from apptest import apptestviews
from webtest import webtestviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('login/', views.login),
    path('logout/', views.logout),
    path('home/', views.home),
    path('product_manage/', proviews.product_manage),
    path('apitest_manage/', views.apitest_manage),
    path('apistep_manage/', views.apistep_manage),
    path('apis_manage/', views.apis_manage),
    path('bug_manage/', bugviews.bug_manage),
    path('set_manage/', setviews.set_manage),
    path('user/', setviews.set_user),
    path('appcase_manage/', apptestviews.appcase_manage),
    path('appcasestep_manage/', apptestviews.appcasestep_manage),
    path('webcase_manage/', webtestviews.webcase_manage),
    path('webcasestep_manage/', webtestviews.webcasestep_manage),
]
