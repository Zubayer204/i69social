from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.

from .models import *

from easy_select2 import select2_modelform

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    list_display = ['username', 'fullName', 'email', 'is_staff', 'is_superuser']
    readonly_fields = ('id','blockedUsers',)
    search_fields = ['id', 'username', 'fullName', 'email']
    exclude = ('password',)

@admin.register(UserSocialProfile)
class UserSocialProfileAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(CoinSettings)
class CoinSettingsAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    pass