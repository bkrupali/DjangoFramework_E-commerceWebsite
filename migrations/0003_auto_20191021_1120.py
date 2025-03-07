# Generated by Django 2.2.6 on 2019-10-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_product_website_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Description',
            field=models.TextField(blank=True, max_length=6000),
        ),
        migrations.AddField(
            model_name='product',
            name='product_cate',
            field=models.CharField(blank=True, choices=[('men', 'men'), ('women', 'women'), ('kids', 'kids')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, choices=[('tshirrt', 'tshirt'), ('shirt', 'shirt'), ('pant', 'pant')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
