from django.db import models
import graphene
from graphene import *
from .models import age, ethnicity, politics, religious, family, zodiacSign,tags
from graphene_django import DjangoObjectType


class ageObj(DjangoObjectType):
    class Meta:
        model = age


class ethnicityObj(DjangoObjectType):
    class Meta:
        model = ethnicity

class familyObj(DjangoObjectType):
    class Meta:
        model = family


class politicsObj(DjangoObjectType):
    class Meta:
        model = politics


class religiousObj(DjangoObjectType):
    class Meta:
        model = religious


class tagsObj(DjangoObjectType):
    class Meta:
        model = tags


class zodiacSignObj(DjangoObjectType):
    class Meta:
        model = zodiacSign


class AllPickers(graphene.ObjectType):
    agePicker = graphene.List(ageObj)
    ethnicityPicker = graphene.List(ethnicityObj)
    familyPicker = graphene.List(familyObj)
    politicsPicker = graphene.List(politicsObj)
    religiousPicker = graphene.List(religiousObj)
    tagsPicker = graphene.List(tagsObj)
    zodiacSignPicker = graphene.List(zodiacSignObj)

    def resolve_agePicker(self, info):
        return age.objects.all()

    def resolve_familyPicker(self, info):
        return family.objects.all()

    def resolve_polticsPicker(self, info):
        return politics.objects.all()

    def resolve_religiousPicker(self, info):
        return religious.objects.all()

    def resolve_tagsPicker(self, info):
        return tags.objects.all()


    def resolve_zodiacSignPicker(self, info):
        return zodiacSign.objects.all()


class Query(graphene.ObjectType):
    defaultPicker = graphene.Field(AllPickers)

    def resolve_defaultPicker(self, info):
        return AllPickers()