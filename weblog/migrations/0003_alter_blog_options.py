# Generated by Django 5.0.6 on 2024-05-22 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('published_at',), 'verbose_name_plural': 'Blogs'},
        ),
    ]
