# Generated by Django 3.2.9 on 2021-12-20 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(max_length=256),
        ),
    ]