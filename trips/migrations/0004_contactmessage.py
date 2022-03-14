# Generated by Django 3.2 on 2022-03-14 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0003_remove_trip_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('messages', models.ManyToManyField(related_name='contact_messages', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_message', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-sent_on'],
            },
        ),
    ]
