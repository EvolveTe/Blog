# Generated by Django 4.2.6 on 2023-10-14 12:05

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True),
        ),
    ]
