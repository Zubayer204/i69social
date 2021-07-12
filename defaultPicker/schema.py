import graphene
from graphene import *
from .models import age, ethnicity, politics, religious, family, zodiacSign,tags
from graphene_django import DjangoObjectType

class ageObj(graphene.ObjectType):
    id = graphene.Int()
    age = graphene.Int()

    def resolve_id(self, info):
        return self['id']

    def resolve_age(self, info):
        return self['age']


class ethnicityObj(graphene.ObjectType):
    id = graphene.Int()
    ethnicity = graphene.String()
    ethnicity_fr = graphene.String()

    def resolve_id(self, info):
        return self['id']

    def resolve_ethnicity(self, info):
        return self['ethnicity']

    def resolve_ethnicity_fr(self, info):
        return self['ethnicity_fr']

class familyObj(graphene.ObjectType):
    id = graphene.Int()
    familyPlans = graphene.String()
    familyPlans_fr = graphene.String()

    def resolve_id(self, info):
        return self['id']

    def resolve_familyPlans(self, info):
        return self['familyPlans']

    def resolve_familyPlans_fr(self, info):
        return self['familyPlans_fr']

class politicsObj(graphene.ObjectType):
    id = graphene.Int()
    politics = graphene.String()
    politics_fr = graphene.String()

    def resolve_id(self, info):
        return self['id']

    def resolve_politics(self, info):
        return self['politics']

    def resolve_politics_fr(self, info):
        return self['politics_fr']

class religiousObj(graphene.ObjectType):
    id = graphene.Int()
    religious = graphene.String()
    religious_fr = graphene.String()

    def resolve_id(self, info):
        return self['id']

    def resolve_ethnicity(self, info):
        return self['religious']

    def resolve_ethnicity(self, info):
        return self['religious_fr']

class tagsObj(graphene.ObjectType):
    id = graphene.Int()
    tag = graphene.String()
    tag_fr = graphene.String()

    def resolve_id(self, info):
        return self['id']

    def resolve_tag(self, info):
        return self['tag']

    def resolve_tag_fr(self, info):
        return self['tag_fr']

class zodiacSignObj(graphene.ObjectType):
    id = graphene.Int()
    zodiacSign = graphene.String()
    zodiacSign_fr = graphene.String()

    def resolve_id(self, info):
        return self['id']

    def resolve_zodiacSign(self, info):
        return self['zodiacSign']

    def resolve_zodiacSign_fr(self, info):
        return self['zodiacSign_fr']



# class AgeType(DjangoObjectType):

#     class Meta:
#         model = 

# class EthnicityType(DjangoObjectType):

#     class Meta:
#         model = ethnicity

# class defaultPickerType(graphene.Union):
#     class Meta:
#         types = (AgeType, EthnicityType)

#     @classmethod
#     def resolve_type(cls, instance, info):
#         # This function tells Graphene what Graphene type the instance is
#         if isinstance(instance, AgeType):
#             return AgeType
#         if isinstance(instance, EthnicityType):
#             return EthnicityType
#         # if isinstance(instance, family):
#         #     return family
#         # if isinstance(instance, politicsObj):
#         #     return politicsObj
#         # if isinstance(instance, religiousObj):
#         #     return religiousObj
#         # if isinstance(instance, tagsObj):
#         #     return tagsObj
#         # if isinstance(instance, zodiacSignObj):
#         #     return zodiacSignObj
#         return defaultPickerType.resolve_type(instance, info)



class SearchResult(graphene.Union):
    class Meta:
        types = (ageObj, ethnicityObj)


class Query(graphene.ObjectType):
    agePicker = graphene.List(ageObj)
    ethnicityPicker = graphene.List(ethnicityObj)
    familyPicker = graphene.List(familyObj)
    politicsPicker = graphene.List(politicsObj)
    religiousPicker = graphene.List(religiousObj)
    tagsPicker = graphene.List(tagsObj)
    zodiacSignPicker = graphene.List(zodiacSignObj)

    defaultPicker = graphene.List(SearchResult)

    def resolve_agePicker(self, info):
        return age.objects.values().all()

    def resolve_familyPicker(self, info):
        return family.objects.values().all()

    def resolve_polticsPicker(self, info):
        return politics.objects.values().all()

    def resolve_religiousPicker(self, info):
        return religious.objects.values().all()

    def resolve_tagsPicker(self, info):
        return tags.objects.values().all()


    def resolve_zodiacSignPicker(self, info):
        return zodiacSign.objects.values().all()

    def resolve_defaultPicker(self, info):
        a = age.objects.all()
        e = ethnicity.objects.all()
        return (a, e)