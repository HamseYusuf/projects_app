# Generated by Django 4.1.5 on 2023-01-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('inprogress', 'inprogress'), ('completed', 'completed')], max_length=100),
        ),
    ]
