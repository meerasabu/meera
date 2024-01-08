# Generated by Django 4.2.5 on 2023-10-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artco', '0004_artist_register_action'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist_register',
            old_name='a_remark',
            new_name='qualification',
        ),
        migrations.RemoveField(
            model_name='artist_register',
            name='a_alterNo',
        ),
        migrations.RemoveField(
            model_name='artist_register',
            name='a_id',
        ),
        migrations.RemoveField(
            model_name='user_register',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user_register',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user_register',
            name='uid',
        ),
        migrations.AddField(
            model_name='artist_register',
            name='a_profilePic',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
