# Generated by Django 3.2 on 2022-03-24 10:13

from django.db import migrations, models
import trips.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20220323_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(validators=[trips.validators.validate_comment]),
        ),
    ]
