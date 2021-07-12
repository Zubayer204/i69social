import secrets
import string
from datetime import datetime, timedelta
from framework import settings
import graphene
from django.contrib.auth import get_user_model
import user.schema
import graphql_jwt
from .api.API_Exception import APIException
import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from user.models import User
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
        username = graphene.String()
        name = graphene.String()
        email = graphene.String()
        gender = graphene.String()
        about = graphene.String()
        location = graphene.String()
        familyPlans = graphene.String()
        age = graphene.String()
        height = graphene.String()
        ethinicity = graphene.String()
        music = graphene.JSONString()
        tvShows = graphene.JSONString()
        sportsTeams  = graphene.JSONString()
        movies = graphene.JSONString()
        work = graphene.String()
        book = graphene.JSONString()
        avatar = graphene.String()

    Output = userResponseObj

    def mutate(self, info, username=None, name=None, gender=None, email=None,height=None,familyPlans=None,
               about=None,url=None,location=None,country=None,age = None, avatar=None):
        global socialObj
        user = info.context.user
        profile = info.context.user
        if username is not None:
            user.username = username
        if name is not None:
            user.name = name
            profile.name = name
        if gender is not None:
            user.gender = gender
            profile.gender = gender
        if email is not None:
            user.email = email
            profile.email = email
        if height is not None:
            profile.height = height
        if familyPlans is not None:
            profile.familyPlans = familyPlans
        if about is not None:
            profile.about = about
        if url is not None:
            profile.url = url
        if location is not None:
            profile.location = location
        if country is not None:
            profile.country = country
        if age is not None:
            profile.age = age
        if avatar is not None:
            profile.avatar = avatar
        user.save()
        profile.save()
        return userResponseObj(id=user.id)

class DeleteProfile(graphene.Mutation):

    class Arguments:
        username = graphene.String()

    Output = userResponseObj

    def mutate(self, info, username):
        try:
            u = User.objects.get(username = username)
            u.delete()
            raise Exception("Account Successfully Deleted")
        except User.DoesNotExist:
            raise Exception('Account does not exist')

class Mutation(
    user.schema.Mutation,
    reports.schema.Mutation,
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