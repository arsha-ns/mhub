# Generated by Django 5.0.3 on 2024-04-01 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='producer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
