import graphene
from .models import *
from .tokenbuilder import generate_agora_token

class generateAgoraToken(graphene.ObjectType):
    id = graphene.String()
    token = graphene.String()
    appID = graphene.String()

    def resolve_id(self, info):
        return self['id']

    def resolve_token(self, info):
        return self['token']

    def resolve_appID(self, info):
        return self['appID']



class Query(graphene.ObjectType):
    generateAgoraToken = graphene.Field(generateAgoraToken, id=graphene.String(required=True), ChannelName=graphene.String(required=True))

    def resolve_generateAgoraToken(self, info, **kwargs):
        id = kwargs.get('id')
        ChannelName = kwargs.get('ChannelName')
        token , appID = generate_agora_token(id, ChannelName)

        tokenlog = AgoraTokenLog.objects.values().first()
        return tokenlog





