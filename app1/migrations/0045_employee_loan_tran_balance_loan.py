# Generated by Django 3.2.22 on 2023-11-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0044_remove_employee_loan_tran_balance_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_loan_tran',
            name='balance_loan',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]