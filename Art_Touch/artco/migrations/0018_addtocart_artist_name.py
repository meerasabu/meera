# Generated by Django 3.2.12 on 2024-01-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artco', '0017_addtocart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='artist_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
