# Generated by Django 3.1.5 on 2021-06-29 07:59

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import framework.validators
import imagekit.models.fields
import user.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='First Name')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female')], null=True)),
                ('about', models.CharField(blank=True, default='', max_length=255, verbose_name='Bio')),
                ('location', models.CharField(blank=True, default='', max_length=255)),
                ('isOnline', models.BooleanField(default=False)),
                ('familyPlans', models.PositiveBigIntegerField(blank=True, choices=[(0, 'Don’t want kids'), (1, 'Want kids'), (2, 'Open to kids'), (3, 'Have kids'), (4, 'Prefer not to say'), (5, "Je ne veux pas d'enfants"), (6, 'Je veux des enfants'), (7, 'Ouvert aux enfants'), (8, "J'ai des enfants"), (9, 'Je préfère ne rien dire')], null=True)),
                ('age', models.PositiveBigIntegerField(blank=True, choices=[(0, '18'), (1, '19'), (2, '20'), (3, '21'), (4, '22'), (5, '23'), (6, '24'), (7, '25'), (8, '26'), (9, '27'), (10, '28'), (11, '29'), (12, '30'), (13, '31'), (14, '32'), (15, '33'), (16, '34'), (17, '35'), (18, '36'), (19, '37'), (20, '38'), (21, '39'), (22, '40'), (23, '41'), (24, '42'), (25, '43'), (26, '44'), (27, '45'), (28, '46'), (29, '47'), (30, '48'), (31, '49'), (32, '50'), (33, '51'), (34, '52'), (35, '53'), (36, '54'), (37, '55'), (38, '56'), (39, '57'), (40, '58'), (41, '59')], null=True)),
                ('politics', models.PositiveBigIntegerField(blank=True, choices=[(0, 'Liberal'), (1, 'Liberal'), (2, 'Conservative'), (3, 'Other'), (4, 'Prefer Not to Say'), (5, 'Libéral'), (6, 'Modéré'), (7, 'Conservateur'), (8, 'Autre'), (9, 'Je préfère ne rien dire')], null=True)),
                ('coins', models.IntegerField(default=0)),
                ('zodiacSign', models.CharField(max_length=200)),
                ('height', models.IntegerField(default=0)),
                ('ethinicity', models.PositiveBigIntegerField(blank=True, choices=[(0, 'American Indian'), (1, 'Black/ African Descent'), (2, 'East Asian'), (3, 'Hispanic / Latino'), (4, 'Middle Eastern'), (5, 'Pacific Islander'), (6, 'South Asian'), (7, 'White / Caucasian'), (8, 'Other'), (9, 'Prefer Not to Say'), (10, 'Amérindien'), (11, 'Noir / Afro Descendant'), (12, "Asie de L'Est"), (13, 'Hispanique / latino'), (14, 'Moyen-Orient'), (15, 'Insulaire du Pacifique'), (16, 'Sud-Asiatique'), (17, 'Blanc / Caucasien'), (18, 'Autre'), (19, 'Je préfère ne rien dire')], null=True)),
                ('religion', models.PositiveBigIntegerField(blank=True, choices=[(0, 'Agnostic'), (1, 'Atheist'), (2, 'Buddhist'), (3, 'Catholic'), (4, 'Christian'), (5, 'Hindu'), (6, 'Jewish'), (7, 'Muslim'), (8, 'Spiritual'), (9, 'Other'), (10, 'Prefer Not to Say'), (10, 'Agnostique'), (11, 'Athée'), (12, 'Bouddhiste'), (13, 'Catholique'), (14, 'Chrétien'), (15, 'Hindou'), (16, 'Juif'), (17, 'Musulman'), (18, 'Spirituel'), (19, 'Autre'), (20, 'Je préfère ne rien dire')], null=True)),
                ('education', models.CharField(max_length=265)),
                ('music', models.JSONField(blank=True, null=True)),
                ('tvShows', models.JSONField(blank=True, null=True)),
                ('sportsTeams', models.JSONField(blank=True, null=True)),
                ('movies', models.JSONField(blank=True, null=True)),
                ('work', models.CharField(blank=True, max_length=265, null=True)),
                ('book', models.JSONField(blank=True, null=True)),
                ('avatar', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=user.models.User.get_avatar_path, validators=[framework.validators.validate_file_size], verbose_name='Avatar')),
                ('blockedUsers', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Interest',
                'verbose_name_plural': 'Interests',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='UserSocialProfile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('platform', models.PositiveSmallIntegerField(choices=[(0, 'Other'), (1, 'Twitter'), (2, 'LinkedIn'), (3, 'Facebook'), (4, 'Instagram')], default=4)),
                ('url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Social Profile',
                'verbose_name_plural': 'User Social Profiles',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='interestedIn',
            field=models.ManyToManyField(blank=True, related_name='interest', to='user.Interests'),
        ),
        migrations.AddField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(related_name='profile_tags', to='user.Tags'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]