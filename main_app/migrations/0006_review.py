# Generated by Django 4.2.19 on 2025-03-06 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_media_imdbid_alter_media_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Good'), (4, '4 - Very Good'), (5, '5 - Excellent')])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
