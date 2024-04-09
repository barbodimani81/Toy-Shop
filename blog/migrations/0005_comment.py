# Generated by Django 4.2.11 on 2024-04-06 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_created_date_category_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Comment', to='blog.post', verbose_name='Comments')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ('id',),
            },
        ),
    ]