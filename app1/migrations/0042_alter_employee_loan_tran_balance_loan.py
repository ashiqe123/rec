# Generated by Django 3.2.22 on 2023-11-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0041_auto_20231123_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_loan_tran',
            name='balance_loan',
            field=models.IntegerField(default=0),
        ),
    ]