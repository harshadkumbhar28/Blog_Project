# Generated by Django 5.0 on 2024-02-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_alter_category_name_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Main_post',
            field=models.BooleanField(default=False),
        ),
    ]
