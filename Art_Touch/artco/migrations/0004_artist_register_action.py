# Generated by Django 4.2.5 on 2023-10-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artco', '0003_artist_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist_register',
            name='action',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
