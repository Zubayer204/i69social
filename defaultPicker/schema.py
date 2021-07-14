from django.db import models
import graphene
from graphene import *
from .models import age, ethnicity, politics, religious, family, zodiacSign,tags
from django.db.models import F


class ageObj(graphene.ObjectType):
    id = graphene.Int()
    value = graphene.Int()
    value_fr = graphene.Int()


class ethnicityObj(graphene.ObjectType):
    id = graphene.Int()
    value = graphene.String()
    value_fr = graphene.String()

class familyObj(graphene.ObjectType):
    id = graphene.Int()
    value = graphene.String()
    value_fr = graphene.String()


class politicsObj(graphene.ObjectType):
    id = graphene.Int()
    value = graphene.String()
    value_fr = graphene.String()


class religiousObj(graphene.ObjectType):
    id = graphene.Int()
    value = graphene.String()
    value_fr = graphene.String()


class tagsObj(graphene.ObjectType):
    id = graphene.Int()
    value = graphene.String()
    value_fr = graphene.String()


class zodiacSignObj(graphene.ObjectType):
    id = graphene.Int()
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
        return age.objects.values('id', value=F('age'), value_fr=F('age'))

    def resolve_ethnicityPicker(self, info):
        return ethnicity.objects.values('id', value=F('ethnicity'), value_fr=F('ethnicity_fr'))

    def resolve_familyPicker(self, info):
        return family.objects.values('id', value=F('familyPlans'), value_fr=F('familyPlans_fr'))

    def resolve_politicsPicker(self, info):
        return politics.objects.values('id', value=F('politics'), value_fr=F('politics_fr'))

    def resolve_religiousPicker(self, info):
        return religious.objects.values('id', value=F('religious'), value_fr=F('religious_fr'))

    def resolve_tagsPicker(self, info):
        return tags.objects.values('id', value=F('tag'), value_fr=F('tag_fr'))


    def resolve_zodiacSignPicker(self, info):
        return zodiacSign.objects.values('id', value=F('zodiacSign'), value_fr=F('zodiacSign_fr'))


class Query(graphene.ObjectType):
    defaultPicker = graphene.Field(AllPickers)

    def resolve_defaultPicker(self, info):
        return AllPickers()