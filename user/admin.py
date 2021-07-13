from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.

from .models import *

from easy_select2 import select2_modelform

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    readonly_fields = ('id',)

@admin.register(UserSocialProfile)
class UserSocialProfileAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    pass

@admin.register(Tags)
class TagsAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(CoinSettings)
class CoinSettingsAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    pass