# Generated by Django 5.2 on 2025-04-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EbayCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=100, unique=True)),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EbayProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('Startprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category_id', models.CharField(max_length=100)),
                ('condition', models.IntegerField()),
                ('stock_quantity', models.IntegerField()),
            ],
        ),
    ]
