# Generated by Django 3.1.6 on 2021-05-18 02:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Warehouse', '0001_initial'),
        ('Product', '0002_product_provider'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('People', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutputBill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('flag', models.IntegerField(choices=[(1, 'Pending'), (0, 'Out for delivery'), (-1, 'Delivered')], default=1)),
                ('output_date', models.DateField(default=datetime.datetime.today, verbose_name='Date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='output_bills', to='People.customer')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InputBill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('flag', models.IntegerField(choices=[(1, 'Pending'), (0, 'Out for delivery'), (-1, 'Delivered')], default=1)),
                ('input_date', models.DateField(default=datetime.datetime.today, verbose_name='Date')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_bills', to='People.provider')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetailOutputBill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=10000)),
                ('output_bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bill.outputbill')),
                ('warehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Warehouse.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='DetailInputBill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=10000)),
                ('input_bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bill.inputbill')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product.product')),
            ],
        ),
    ]
