# Generated by Django 2.1.13 on 2020-01-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='billview',
            name='lastupdated',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
