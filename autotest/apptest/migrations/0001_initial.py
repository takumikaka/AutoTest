# Generated by Django 2.1.7 on 2019-04-28 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20190425_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appcasename', models.CharField(max_length=200, verbose_name='Case_Name')),
                ('apptestresult', models.BooleanField(verbose_name='Test_Result')),
                ('apptester', models.CharField(max_length=16, verbose_name='Tester')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create_Time')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': 'App_TestCase',
                'verbose_name_plural': 'App_TestCase',
            },
        ),
        migrations.CreateModel(
            name='Appcasestep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appteststep', models.CharField(max_length=200, verbose_name='Test_Step')),
                ('apptestobjname', models.CharField(max_length=200, verbose_name='Test_Object_Name')),
                ('appfindmethod', models.CharField(max_length=200, verbose_name='Find_Method')),
                ('appevelement', models.CharField(max_length=800, verbose_name='Evelement')),
                ('appoptmethod', models.CharField(max_length=200, verbose_name='Operate_Method')),
                ('apptestdata', models.CharField(max_length=200, null=True, verbose_name='Test_Data')),
                ('appassertdata', models.CharField(max_length=200, verbose_name='Assert_Data')),
                ('apptestresult', models.BooleanField(verbose_name='Test_Result')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create_Time')),
                ('Appcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptest.Appcase')),
            ],
        ),
    ]
