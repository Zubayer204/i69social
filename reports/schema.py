from reports.models import Reported_Users
from reports.models import GoogleAuth
import graphene
from user.models import *
from django.db.models import F
from framework.api.API_Exception import APIException
from graphql_jwt.decorators import login_required
import graphql_social_auth
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth import get_user_model



class reportResponseObj(graphene.ObjectType):
    id = graphene.String()

class reportUser(graphene.Mutation):

    class Arguments:
        timestamp = graphene.DateTime()
        reporter = graphene.String()
        reportee = graphene.String()

    Output = reportResponseObj

    def mutate(self, info, timestamp,reporter,reportee):
        report = Reported_Users.objects.create(
                timestamp=timestamp,
                reporter=reporter,
                reportee=reportee,
            )
        user = get_user_model().objects.get(id=reporter)
        blckd_user = get_user_model().objects.get(id=reportee)
        user.blockedUsers.add(blckd_user)
        report.save()
        print(Reported_Users.id)
        return reportResponseObj(id=report.id)

class googleAuthResponse(graphene.ObjectType):
    email = graphene.String()
    azp = graphene.String()
    aup = graphene.String()
    sub = graphene.String()
    is_new = graphene.Boolean()

class googleAuth(graphene.Mutation):
    class Arguments:
        access_token = graphene.String(required=True)

    Output = googleAuthResponse

    def mutate(self, info, access_token):
        try:
            CLIENT_ID = "403376972935-5j0a2u4mi83qkuec1k7moqj50sl0857p.apps.googleusercontent.com"
            idinfo = id_token.verify_oauth2_token(access_token, requests.Request(), CLIENT_ID)

            if GoogleAuth.objects.get(email=idinfo['email']):
                is_new = False

            else:
                user = get_user_model().objects.create(
                    password='',
                    name=idinfo['name'],
                    email=idinfo['email'],
                    username=idinfo['email'].split('@')[0]
                )
                user.save()
                is_new = True
                g = GoogleAuth.objects.create(
                    email=idinfo['email'],
                    sub=idinfo['sub']
                )
                g.save()


            return googleAuthResponse(email=idinfo['email'], azp=idinfo['azp'], aup=idinfo['aup'], sub=idinfo['sub'], is_new=is_new)
        except ValueError:
            Exception("Invalid Token")
    


class Mutation(graphene.ObjectType):
    social_auth = graphql_social_auth.SocialAuth.Field()
    reportUser = reportUser.Field()
    google_auth = googleAuth.Field()


# class googleAuth(graphene.ObjectType):
    
