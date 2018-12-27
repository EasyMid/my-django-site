# Generated by Django 2.1.2 on 2018-12-23 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='title',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]