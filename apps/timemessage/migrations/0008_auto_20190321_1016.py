# Generated by Django 2.1.7 on 2019-03-21 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timemessage', '0007_auto_20190320_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sourcevideo',
            old_name='img_url',
            new_name='video_url',
        ),
    ]
