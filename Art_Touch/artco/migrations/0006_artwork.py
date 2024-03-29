# Generated by Django 4.2.5 on 2023-10-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artco', '0005_rename_a_remark_artist_register_qualification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('work', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('price', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
