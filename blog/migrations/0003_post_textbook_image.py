# Generated by Django 2.1.15 on 2021-07-03 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='textbook_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
