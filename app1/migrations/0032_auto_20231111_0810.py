# Generated by Django 3.2.22 on 2023-11-11 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_purchasepayment_bank_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='salescreditnote1',
            name='billno',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salescreditnote1',
            name='rem_qty',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='deletedcreditnotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=50)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]