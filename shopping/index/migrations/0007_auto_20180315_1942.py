# Generated by Django 2.0.3 on 2018-03-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20180315_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spider_porduct',
            name='sname',
            field=models.CharField(max_length=1000),
        ),
    ]