# Generated by Django 3.0.7 on 2020-06-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200612_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]