# Generated by Django 3.2.12 on 2023-11-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artco', '0010_auto_20231128_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='item_image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
