# Generated by Django 4.2.11 on 2024-04-07 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Comments', to='blog.post', verbose_name='Comments'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Image', to='blog.post', verbose_name='Images')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]