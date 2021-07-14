import secrets
import string
from datetime import datetime, timedelta
from framework import settings
import graphene
from django.contrib.auth import get_user_model
import user.schema
import purchase.schema
import graphql_jwt
from .api.API_Exception import APIException
import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from user.models import User, UserSocialProfile
from defaultPicker.models import tags
import reports.schema
#import purchase.schema
import defaultPicker.schema
import chatapp.schema
class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class userResponseObj(graphene.ObjectType):
    id = graphene.String()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class UpdateProfile(graphene.Mutation):

    class Arguments:
        id = graphene.String()
        username = graphene.String()
        fullName = graphene.String()
        email = graphene.String()
        gender = graphene.Int()
        about = graphene.String()
        location = graphene.String()
        about = graphene.String()
        isOnline = graphene.Boolean()
        familyPlans = graphene.Int()
        age = graphene.Int()
        tag_ids = graphene.List(graphene.Int)
        politics = graphene.Int()
        zodiacSign = graphene.String()
        height = graphene.String()
        interested_in = graphene.Int()
        ethinicity = graphene.String()
        religion = graphene.Int()
        education = graphene.String()
        music = graphene.JSONString()
        tvShows = graphene.JSONString()
        sportsTeams  = graphene.JSONString()
        movies = graphene.JSONString()
        work = graphene.String()
        book = graphene.JSONString()
        avatar = graphene.String()

        url = graphene.String()
        platform = graphene.String()

    Output = userResponseObj

    def mutate(self, info, id, username=None, fullName=None, gender=None, email=None,height=None,familyPlans=None,
               about=None,location=None,age = None, avatar=None, isOnline=None, tag_ids=None, url=None, platform=None,
               politics=None, zodiacSign=None, interested_in=None, ethnicity=None, religion=None, education=None):
        global socialObj
        user = get_user_model().objects.get(id=id)
        try:
            profile = UserSocialProfile.objects.get(user=user)
        except:
            profile = None
        if username is not None:
            user.username = username
        if fullName is not None:
            user.fullName = fullName
        if gender is not None:
            user.gender = gender
        if email is not None:
            user.email = email
        if height is not None:
            user.height = height
        if familyPlans is not None:
            user.familyPlans = familyPlans
        if about is not None:
            user.about = about
        if location is not None:
            user.location = location
        if age is not None:
            user.age = age
        if avatar is not None:
            user.avatar = avatar
        if isOnline is not None:
            user.isOnline = isOnline
        if tag_ids is not None:
            for tag_id in tag_ids:
                tag = tags.objects.get(id=tag_id)
                if tag is not None:
                    user.tags.add(tag)
        if politics is not None:
            user.politics = politics
        if zodiacSign is not None:
            user.zodiacSign = zodiacSign
        if  interested_in is not None:
            user.interested_in = interested_in
        if ethnicity is not None:
            user.ethnicity = ethnicity
        if religion is not None:
            user.religion = religion
        if education is not None:
            user.education = education

        if url is not None or platform is not None:
            if profile is None:
                new_profile = UserSocialProfile.objects.create(url=url, platform=platform, user=user)
                new_profile.save()
            else:
                if url is not None:
                    profile.url = url
                    profile.save()
                if platform is not None:
                    profile.platform = platform
                    profile.save()

        
        user.save()
        return userResponseObj(id=user.id)

class DeleteProfile(graphene.Mutation):

    class Arguments:
        id = graphene.String()

    Output = userResponseObj

    def mutate(self, info, id):
        try:
            u = User.objects.get(id = id)
            u.delete()
            raise Exception("Account Successfully Deleted")
        except User.DoesNotExist:
            raise Exception('Account does not exist')

class Mutation(
    user.schema.Mutation,
    reports.schema.Mutation,
    purchase.schema.Mutation,
    graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()
    updateProfile = UpdateProfile.Field()
    deleteProfile = DeleteProfile.Field()


class Query(
    #travel_log_data.schema.Query,
    defaultPicker.schema.Query,
    chatapp.schema.Query,
    user.schema.Query,
    graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, username=graphene.String(required=True))

    def resolve_users(self, info):
        return get_user_model().objects.all()

    @staticmethod
    def resolve_user(self, info, **kwargs):
        username = kwargs.get('username')
        if username is not None:
            return get_user_model().objects.get(username=username)
        else:
            raise Exception('Username is a required parameter')


schema = graphene.Schema(query=Query, mutation=Mutation)