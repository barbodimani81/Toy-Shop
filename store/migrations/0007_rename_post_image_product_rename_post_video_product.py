# Generated by Django 4.2.11 on 2024-04-08 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_post_comment_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='post',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='post',
            new_name='product',
        ),
    ]
