# Generated by Django 5.1.1 on 2024-09-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profs',
            name='code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
