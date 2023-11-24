# Generated by Django 3.2.22 on 2023-11-07 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0028_auto_20231106_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasebill',
            name='account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='cheque_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='customer_gstin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='customer_gsttype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='is_from_purchase_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='purchase_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchaseorder'),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='purchase_order_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='upi_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='vendor_balance',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='vendor_gstin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='vendor_gsttype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='cheque_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='customer_gstin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='customer_gsttype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='is_from_purchase_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='upi_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='vendor_balance',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='vendor_gstin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='vendor_gsttype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='creditlimit',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasebill',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Billed', 'Billed'), ('Save', 'Save')], default='Draft', max_length=150),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Approved', 'Approved'), ('Save', 'Save'), ('Billed', 'Billed')], default='Draft', max_length=150),
        ),
        migrations.CreateModel(
            name='VendorComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app1.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_comments', to='app1.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBillComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_comments', to='app1.purchasebill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConvertBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.purchasebill')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.purchaseorder')),
            ],
        ),
    ]
