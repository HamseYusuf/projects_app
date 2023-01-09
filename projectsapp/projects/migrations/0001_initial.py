# Generated by Django 4.1.5 on 2023-01-09 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('technology', models.CharField(max_length=100)),
                ('developers', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('new', 'new'), ('inprogreess', 'inprogress'), ('completed', 'completed')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
