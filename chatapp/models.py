from django.db import models

# Create your models here.
import json

from django.db import models

from django.conf import settings
import uuid

class AgoraTokenLog(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4,null=False)
    token = models.CharField(max_length=265,null=False)
    appID = models.CharField(max_length=265, null=False)
    creator = models.CharField(max_length=265,null=False)


    def __str__(self):
        return (self.token + ' - ' + ' - ' + self.creator)

