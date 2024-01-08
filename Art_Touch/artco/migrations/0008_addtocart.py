# Generated by Django 3.2.12 on 2023-11-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artco', '0007_artwork_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.IntegerField(null=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('item_id', models.FileField(null=True, upload_to='')),
                ('item', models.CharField(max_length=30, null=True)),
                ('qnty', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
            ],
        ),
    ]