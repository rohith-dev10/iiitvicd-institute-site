# Generated by Django 4.1.3 on 2022-11-27 11:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('head', models.CharField(max_length=200)),
                ('detail', models.TextField()),
            ],
        ),
    ]
