# Generated by Django 3.1.2 on 2020-10-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
