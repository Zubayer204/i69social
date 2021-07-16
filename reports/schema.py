from reports.models import Reported_Users
from reports.models import GoogleAuth
import graphene
from user.models import *
from django.db.models import F
from framework.api.API_Exception import APIException
import requests
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
    is_new = graphene.Boolean()
    id = graphene.String()

class SocialAuth(graphene.Mutation):
    class Arguments:
        access_token = graphene.String(required=True)
        provider = graphene.String(required=True)

    Output = googleAuthResponse

    def mutate(self, info, access_token, provider):
        try:
            if 'google' in provider.lower():
                print(access_token)
                idinfo = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={access_token}")
                idinfo = idinfo.json()
                print(idinfo)
                if idinfo.get('error') == "invalid_token":
                    return Exception("Invalid Token")

            if GoogleAuth.objects.get(email=idinfo['email']):
                is_new = False
                user = get_user_model().objects.get(email=idinfo['email'])

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


            return googleAuthResponse(email=idinfo['email'], is_new=is_new, id=user.id)
        except ValueError:
            Exception("Invalid Token")
    


class Mutation(graphene.ObjectType):
    social_auth = SocialAuth.Field()
    reportUser = reportUser.Field()


# class googleAuth(graphene.ObjectType):
    
