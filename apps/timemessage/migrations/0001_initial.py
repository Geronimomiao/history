# Generated by Django 2.1.7 on 2019-03-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=100, null=True, verbose_name='事件发生年代')),
                ('month', models.CharField(blank=True, max_length=100, null=True, verbose_name='事件发生月份')),
                ('location', models.CharField(blank=True, max_length=50, null=True, verbose_name='事件发生地点')),
                ('event_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='事件名称')),
                ('event_message', models.TextField(blank=True, null=True, verbose_name='事件内容')),
            ],
            options={
                'verbose_name': '事件信息记录',
                'verbose_name_plural': '事件信息记录',
            },
        ),
    ]
