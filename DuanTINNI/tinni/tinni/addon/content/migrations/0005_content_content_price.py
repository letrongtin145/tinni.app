# Generated by Django 5.0.4 on 2024-06-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_content_content_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='content_price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
