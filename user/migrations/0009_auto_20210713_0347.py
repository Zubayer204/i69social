# Generated by Django 3.1.5 on 2021-07-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20210712_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='interestedIn',
        ),
        migrations.AddField(
            model_name='user',
            name='interestedIn',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'SERIOUS_RELATIONSHIP_ONLY_MALE'), (2, 'SERIOUS_RELATIONSHIP_ONLY_FEMALE'), (3, 'SERIOUS_RELATIONSHIP_BOTH'), (4, 'CAUSAL_DATING_ONLY_MALE'), (5, 'CAUSAL_DATING_ONLY_FEMALE'), (6, 'CAUSAL_DATING_BOTH'), (7, 'NEW_FRIENDS_ONLY_MALE'), (8, 'NEW_FRIENDS_ONLY_FEMALE'), (9, 'NEW_FRIENDS_BOTH'), (10, 'ROOM_MATES_ONLY_MALE'), (11, 'ROOM_MATES_ONLY_FEMALE'), (12, 'ROOM_MATES_BOTH'), (13, 'BUSINESS_CONTACTS_ONLY_MALE'), (14, 'BUSINESS_CONTACTS_ONLY_FEMALE'), (15, 'BUSINESS_CONTACTS_BOTH')], null=True),
        ),
        migrations.DeleteModel(
            name='Interests',
        ),
    ]
