import uuid
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from framework.utils import SOCIAL_PROFILE_PLATFORMS
from django.conf import settings

from framework.validators import validate_file_size, processed_image_field_specs
from gallery.models import Album
from imagekit.models import ProcessedImageField
import uuid
from .utils import FAMILY_CHOICE, AGE_RANGE, ETHINICITY_TYPE, POLITICS_CHOICE, RELIGIOUS_CHOICE
from django.contrib.auth import get_user_model


class Tags(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"

    def __str__(self):
        return self.name


class User(AbstractUser):
    def get_avatar_path(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'static/uploads/images/avatar/' + filename

    INTEREST_CHOICES = (
        (1, "SERIOUS_RELATIONSHIP_ONLY_MALE"),
        (2, "SERIOUS_RELATIONSHIP_ONLY_FEMALE"),
        (3, "SERIOUS_RELATIONSHIP_BOTH"),

        (4, "CAUSAL_DATING_ONLY_MALE"),
        (5, "CAUSAL_DATING_ONLY_FEMALE"),
        (6, "CAUSAL_DATING_BOTH"),

        (7, "NEW_FRIENDS_ONLY_MALE"),
        (8, "NEW_FRIENDS_ONLY_FEMALE"),
        (9, "NEW_FRIENDS_BOTH"),

        (10, "ROOM_MATES_ONLY_MALE"),
        (11, "ROOM_MATES_ONLY_FEMALE"),
        (12, "ROOM_MATES_BOTH"),

        (13, "BUSINESS_CONTACTS_ONLY_MALE"),
        (14, "BUSINESS_CONTACTS_ONLY_FEMALE"),
        (15, "BUSINESS_CONTACTS_BOTH")
    )
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
    )



    id = models.UUIDField(primary_key=True,default = uuid.uuid4, editable=False,null=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = None
    last_name = None
    fullName = models.CharField(max_length=255, default='', blank=True, verbose_name='Full Name')
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    about = models.CharField(max_length=255, default='', blank=True, verbose_name='Bio')
    location = models.CharField(max_length=255, default='', blank=True)
    isOnline = models.BooleanField(default=False)
    familyPlans = models.PositiveBigIntegerField(choices=FAMILY_CHOICE, null=True, blank=True)
    age = models.PositiveBigIntegerField(choices=AGE_RANGE, blank=True, null=True)
    tags = models.ManyToManyField(Tags, related_name='profile_tags', blank=True)
    politics = models.PositiveBigIntegerField(choices=POLITICS_CHOICE, blank=True, null=True)
    coins = models.PositiveIntegerField(null=False,default=0)
    zodiacSign = models.CharField(max_length=200, null=True, blank=True)
    height = models.IntegerField(null=False,default=0)
    # interestedIn = models.ManyToManyField(Interests, blank=True,related_name='interest')
    interestedIn = models.PositiveSmallIntegerField(choices=INTEREST_CHOICES, null=True, blank=True)
    ethinicity = models.PositiveBigIntegerField(choices=ETHINICITY_TYPE, blank=True, null=True)
    religion = models.PositiveBigIntegerField(choices=RELIGIOUS_CHOICE, blank=True, null=True)
    blockedUsers =  models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    education = models.CharField(max_length=265, null=True, blank=True)
    music = models.JSONField(encoder=None,null=True, blank=True)
    tvShows = models.JSONField(encoder=None,null=True, blank=True)
    sportsTeams = models.JSONField(encoder=None,null=True, blank=True)
    movies = models.JSONField(encoder=None,null=True, blank=True)
    work = models.CharField(max_length=265,null=True, blank=True)
    book = models.JSONField(encoder=None,null=True, blank=True)


    avatar = ProcessedImageField(
        blank=True,
        verbose_name='Avatar',
        upload_to=get_avatar_path,
        null=True,
        validators=[validate_file_size],
        **processed_image_field_specs
    )

class UserSocialProfile(models.Model):


    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.PositiveSmallIntegerField(choices=SOCIAL_PROFILE_PLATFORMS, default=4)
    url = models.URLField()

    class Meta:
        verbose_name_plural = "User Social Profiles"
        verbose_name = "User Social Profile"

    def __str__(self):
        return str(self.user.username) + ' - ' + str(self.platform)


class CoinSettings(models.Model):
    method = models.CharField(max_length=70)
    coins_needed = models.IntegerField()

    def __str__(self):
        return self.method + " --- " + str(self.coins_needed)
