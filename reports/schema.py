from reports.models import Reported_Users
import graphene
from user.models import *
from django.db.models import F
from framework.api.API_Exception import APIException
from graphql_jwt.decorators import login_required
import graphql_social_auth



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
        report.save()
        print(Reported_Users.id)
        return reportResponseObj(id=report.id)


class Mutation(graphene.ObjectType):
    social_auth = graphql_social_auth.SocialAuth.Field()
    reportUser = reportUser.Field()
