# Generated by Django 3.1.5 on 2021-06-29 12:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgoraTokenLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('token', models.CharField(editable=False, max_length=265)),
                ('appID', models.CharField(editable=False, max_length=265)),
                ('creator', models.CharField(editable=False, max_length=265)),
            ],
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]