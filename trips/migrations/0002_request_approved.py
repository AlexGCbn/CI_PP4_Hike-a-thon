# Generated by Django 3.2 on 2022-02-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]