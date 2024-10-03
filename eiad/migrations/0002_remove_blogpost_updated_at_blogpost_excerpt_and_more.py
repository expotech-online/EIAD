# Generated by Django 5.1.1 on 2024-10-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eiad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='excerpt',
            field=models.TextField(default='No excerpt available'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]
