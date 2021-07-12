import os
import time
import json

from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from .src.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
from .models import AgoraTokenLog
from user.models import User

def generate_agora_token(id, channelName):
    user = User.objects.get(id=id)
    appID = 'AGORA_APP_ID'
    appCertificate = 'AGORA_APP_CERTIFICATE'
    channelName = channelName
    userAccount = user.username
    expireTimeInSeconds = 3600
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds

    token = RtcTokenBuilder.buildTokenWithAccount(
        appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)

    log = AgoraTokenLog(token = token, appID = appID, creator = userAccount)
    log.save()
    print(token)
    print('done token')

    return (token , appID)