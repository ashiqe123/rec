# Generated by Django 3.2.22 on 2023-11-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0033_auto_20231111_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='salescreditnote1',
            name='stock',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
