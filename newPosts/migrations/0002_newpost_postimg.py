# Generated by Django 4.2.5 on 2023-10-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newPosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='postImg',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='images/'),
        ),
    ]
