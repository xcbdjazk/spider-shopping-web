# Generated by Django 2.0.3 on 2018-03-15 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20180315_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spider_Porduct_item',
            fields=[
                ('spid', models.AutoField(primary_key=True, serialize=False)),
                ('option_url', models.CharField(max_length=20)),
                ('option_product', models.CharField(max_length=32)),
            ],
        ),
    ]