# Generated by Django 2.0.3 on 2018-03-15 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_spider_porduct_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spider_porduct',
            old_name='user',
            new_name='spider',
        ),
    ]
