from django.db import models
import graphene
from graphene import *
from .models import age, ethnicity, politics, religious, family, zodiacSign,tags
from graphene_django import DjangoObjectType
from django.db.models import F


class ageObj(graphene.ObjectType):
    id = graphene.String()
    value = graphene.String()
    value_fr = graphene.String()


class ethnicityObj(graphene.ObjectType):
    id = graphene.String()
    value = graphene.String()
    value_fr = graphene.String()

class familyObj(graphene.ObjectType):
    id = graphene.String()
    value = graphene.String()
    value_fr = graphene.String()


class politicsObj(graphene.ObjectType):
    id = graphene.String()
    value = graphene.String()
    value_fr = graphene.String()


class religiousObj(graphene.ObjectType):
    id = graphene.String()
    value = graphene.String()
    value_fr = graphene.String()


class tagsObj(graphene.ObjectType):
    id = graphene.String()
    value = graphene.String()
    value_fr = graphene.String()


class zodiacSignObj(graphene.ObjectType):
    id = graphene.String()
    value = graphene.String()
    value_fr = graphene.String()


class AllPickers(graphene.ObjectType):
    agePicker = graphene.List(ageObj)
    ethnicityPicker = graphene.List(ethnicityObj)
    familyPicker = graphene.List(familyObj)
    politicsPicker = graphene.List(politicsObj)
    religiousPicker = graphene.List(religiousObj)
    tagsPicker = graphene.List(tagsObj)
    zodiacSignPicker = graphene.List(zodiacSignObj)

    def resolve_agePicker(self, info):
        return age.objects.values('id', value=F('age'), valueFr=F('age_fr'))

    def resolve_ethnicityPicker(self, info):
        return ethnicity.objects.values('id', value=F('ethnicity'), valueFr=F('ethnicity_fr'))

    def resolve_familyPicker(self, info):
        return family.objects.values('id', value=F('familyPlans'), valueFr=F('familyPlans_fr'))

    def resolve_polticsPicker(self, info):
        return politics.objects.values('id', value=F('politics'), valueFr=F('politics_fr'))

    def resolve_religiousPicker(self, info):
        return religious.objects.values('id', value=F('religious'), valueFr=F('religious_fr'))

    def resolve_tagsPicker(self, info):
        return tags.objects.values('id', value=F('tag'), valueFr=F('tag_fr'))


    def resolve_zodiacSignPicker(self, info):
        return zodiacSign.objects.values('id', value=F('zodiacSign'), valueFr=F('zodiacSign_fr'))


class Query(graphene.ObjectType):
    defaultPicker = graphene.Field(AllPickers)

    def resolve_defaultPicker(self, info):
        return AllPickers()