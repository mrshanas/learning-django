# Generated by Django 4.0 on 2022-01-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
