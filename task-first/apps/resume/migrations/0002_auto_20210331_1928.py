# Generated by Django 2.2.19 on 2021-03-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeitem',
            name='photo',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]
