from framework.api.API_Exception import APIException
import graphene
from user.models import *
#from framework.api.API_Exception import APIException
from gallery.models import Photo
from gallery.schema import PhotoObj
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
    id = graphene.String()
    success = graphene.Boolean()
    image_data = graphene.String()

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
        image_data = graphene.String()

    def mutate(self, info,  id=None, image_data=None):
        user = User.objects.get(id=id)
        avatar = image_data
        user.avatar = avatar
        user.save()
        return UploadFileObj(id=user.id, image_data=user.avatar, success=True)

class blockUser(graphene.Mutation):
    Output = blockResponseObj

    class Arguments:
        id = graphene.String()
        blocked_id = graphene.String()

    def mutate(self, info, id, blocked_id):
        blckd_user = User.objects.get(id=blocked_id)
        user = User.objects.get(id=id)
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
    photos = graphene.List(PhotoObj, id=graphene.String(required=True))
    blockedUsers = graphene.List(blockedUsers)
    search_users = graphene.List(
        searchObj,
        interested_in=graphene.Int(required=True),
        min_height=graphene.Int(),
        max_height=graphene.Int(),
        min_age=graphene.Int(),
        max_age=graphene.Int(),
        description="Search users based on their age, interest, height or gender"
    )


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

    def resolve_blockedUsers(self, info):
        id = info.context.user.id
        user = User.objects.get(id=id)
        return user.blockedUsers.all().values('id', 'username')
    
    @staticmethod
    def resolve_search_users(self, info, **kwargs):
        interest= kwargs.get('interested_in')
        max_age = kwargs.get('max_age')
        min_age = kwargs.get('min_age')
        max_height = kwargs.get('max_height')
        min_height = kwargs.get('min_height')

        if interest is not None:
            res = get_user_model().objects.filter(interestedIn=interest)
        
        if max_age is not None or min_age is not None:
            if max_age is None:
                max_age = 100
            if min_age is None:
                min_age = 0
            res = res.filter(age__range=(min_age, max_age))

        if max_height is not None or min_height is not None:
            if max_height is None:
                max_height = 1000
            if min_height is None:
                min_height = 0
            res = res.filter(height__range=(min_height, max_height))
        
        return res

    def resolve_photos(self, info, **kwargs):
        id = kwargs.get('id')
        if id is None:
            return Exception("Id is a required parameter")
        user = get_user_model().objects.get(id=id)
        return Photo.objects.filter(user=user)

class Mutation(graphene.ObjectType):
    updateCoin = updateCoin.Field()
    UpdateProfilePic = UpdateProfilePic.Field()
    blockUser = blockUser.Field()
    deductCoin = ChatCoin.Field()
