# Generated by Django 3.2.12 on 2024-01-02 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artco', '0015_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='artist_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
