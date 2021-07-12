from framework.api.API_Exception import APIException
import graphene
from user.models import *
from django.db.models import F
#from framework.api.API_Exception import APIException
from graphql_jwt.decorators import login_required
from gallery.models import Album
from gallery.schema import AlbumObj
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from .utils import get_gender_from_code

class Gender(graphene.ObjectType):
    code = graphene.String()
    name = graphene.String()

    def resolve_code(self, info):
        return self
    
    def resolve_name(self, info):
        return get_gender_from_code(self)
class photosObj(graphene.ObjectType):
    album = graphene.Field(AlbumObj)

    def resolve_album(self, info):
        return Album.objects.values().get(id=self['album_id'])


class isOnlineObj(graphene.ObjectType):
    id = graphene.String()
    isOnline = graphene.Boolean()
    username = graphene.String()

    def resolve_isOnline(self, info):
        return self['isOnline']

    def resolve_username(self, info):
        return self['username']

    def resolve_id(self, info):
        return self['id']

class OnlineObj(graphene.ObjectType):
    isOnline = graphene.Boolean()

    def resolve_isOnline(self, info):
        if isinstance(self, User):
            return self.isOnline

class UploadFileObj(graphene.ObjectType):
    fileName = graphene.String()


class coinsResponseObj(graphene.ObjectType):
    id = graphene.String()
    coins = graphene.Int()
    success = graphene.Boolean()

class blockResponseObj(graphene.ObjectType):
    id = graphene.String()
    username = graphene.String()
    success = graphene.Boolean()


class updateCoin(graphene.Mutation):

    class Arguments:
        coins = graphene.Int()
        id = graphene.String()

    Output = coinsResponseObj

    def mutate(self, info, coins=None, id=None):
        user = User.objects.get(id=id)
        coin = user.coins
        print(coin)

        if coins is not None:
            user.coins = coins + coin

        user.save()
        return coinsResponseObj(id=user.id, success=True, coins=user.coins)

class ChatCoin(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        method = graphene.String()

    Output = coinsResponseObj

    def mutate(self, info, method=None, id=None):
        user = User.objects.get(id=id)
        if user.is_anonymous:
            return APIException("You must be logged in to use coins")
        coin = user.coins
        print(coin)
        # if method.upper() == "MESSAGE":
        #     if coin < 19:
        #         return APIException("Insufficient Coins")
            
        #     user.coins = coin - 19

        # if method.upper() == "IMAGE_MESSAGE":
        #     if coin < 60:
        #         return APIException("Insufficient Coins")
            
        #     user.coins = coin - 60
        coin_settings = CoinSettings.objects.all()
        for coin_setting in coin_settings:
            if method.upper() == coin_setting.method.upper():
                if coin < coin_setting.coins_needed:
                    return APIException("Insufficient Coins")
                user.coins = coin - coin_setting.coins_needed
                break
        else:
            return APIException("Please enter a valid method")

        user.save()
        return coinsResponseObj(id=user.id, success=True, coins=user.coins)


class UpdateProfilePic(graphene.Mutation):
    Output = UploadFileObj

    class Arguments:
        id = graphene.String()

    def mutate(self, info,  id=None):
        user = User.objects.get(id=id)
        avatar = info.context.FILES['imageFile']
        profile = User.objects.get(user=user)
        profile.avatar = avatar
        profile.save()
        user.save()
        return UploadFileObj(fileName=profile.profile_pic)

class blockUser(graphene.Mutation):
    Output = blockResponseObj

    class Arguments:
        id = graphene.String()

    @login_required
    def mutate(self, info, id):
        blckd_user = User.objects.get(id=id)
        user = User.objects.get(id=info.context.user.id)
        user.blockedUsers.add(blckd_user)
        user.save()
        return blockResponseObj(id=blckd_user.id, username=blckd_user.username, success=True)


class searchObj(DjangoObjectType):
    class Meta:
        model = get_user_model()


class blockedUsers(graphene.ObjectType):
    id = graphene.String()
    username = graphene.String()

    def resolve_id(self, info):
        return self['id']
    
    def resolve_username(self, info):
        return self['username']


class Query(graphene.ObjectType):

    usersOnline = graphene.List(isOnlineObj)

    isOnline = graphene.Field(OnlineObj, id=graphene.String(required=True))

    photos = graphene.Field(photosObj, id=graphene.String(required=True))

    blockedUsers = graphene.List(blockedUsers)

    gender_search_users = graphene.List(searchObj, gender=graphene.Int(required=True), description = "Search users based on gender")

    height_search_users = graphene.List(searchObj, min_height=graphene.String(required=True),max_height=graphene.String(required=True), description = "Search users based on height")

    age_search_users = graphene.List(searchObj, min_age=graphene.String(required=True),max_age=graphene.String(required=True), description = "Search users based on age")

    interest_search_users = graphene.List(searchObj, interest=graphene.String(required=True), description = "Search users based on their interest")


    def resolve_usersOnline(self, info):
        try:
            return User.objects.filter(isOnline=True).values('isOnline','username','id')
        except:
            raise Exception("try again")

    def resolve_isOnline(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            user = User.objects.get(id=id)
            return user
        else:
            raise Exception('Id is a required parameter')

    @login_required
    def resolve_blockedUsers(self, info):
        id = info.context.user.id
        user = User.objects.get(id=id)
        return user.blockedUsers.all().values('id', 'username')


    @staticmethod
    def resolve_gender_search_users(self, info, **kwargs):
        gender = kwargs.get('gender')
        if gender is not None:
            print(gender)
            print(get_user_model().objects.filter(gender=gender))
            return get_user_model().objects.filter(gender=gender)
        elif gender == "Both":
            return get_user_model().objects.values().all()
        else:
            raise Exception('gender is a required parameter')

    @staticmethod
    def resolve_height_search_users(self, info, **kwargs):
        min_height = kwargs.get('min_height')
        max_height = kwargs.get('max_height')
        if min_height and max_height is not None:
            return get_user_model().objects.filter(height__range=(min_height, max_height))
        else:
            raise Exception('No user found')

    @staticmethod
    def resolve_age_search_users(self, info, **kwargs):
        min_age = kwargs.get('min_age')
        max_age = kwargs.get('max_age')
        if min_age and max_age is not None:
            # print(get_user_model().objects.filter(age__range=(min_age, max_age)))
            return get_user_model().objects.filter(age__range=(min_age, max_age))
        else:
            raise Exception('NO user found')

    def resolve_interest_search_users(self, info, **kwargs):
        interest = kwargs.get('interest')
        if interest is not None:
            # print(get_user_model().objects.filter(interestedIn = interest))
            return get_user_model().objects.filter(interestedIn = interest)





class Mutation(graphene.ObjectType):
    updateCoin = updateCoin.Field()
    UpdateProfilePic = UpdateProfilePic.Field()
    blockUser = blockUser.Field()
    deductCoin = ChatCoin.Field()
