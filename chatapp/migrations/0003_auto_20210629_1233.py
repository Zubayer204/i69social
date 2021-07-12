# Generated by Django 3.1.5 on 2021-06-29 12:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_auto_20210629_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agoratokenlog',
            name='appID',
            field=models.CharField(max_length=265),
        ),
        migrations.AlterField(
            model_name='agoratokenlog',
            name='creator',
            field=models.CharField(max_length=265),
        ),
        migrations.AlterField(
            model_name='agoratokenlog',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='agoratokenlog',
            name='token',
            field=models.CharField(max_length=265),
        ),
    ]
