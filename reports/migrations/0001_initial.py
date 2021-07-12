# Generated by Django 3.1.5 on 2021-06-25 22:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reported_Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('reporter', models.CharField(max_length=100)),
                ('reportee', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=255)),
            ],
        ),
    ]
