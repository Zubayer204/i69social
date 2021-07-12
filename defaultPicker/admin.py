from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.

from .models import *

from easy_select2 import select2_modelform

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


@admin.register(age)
class AgeAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    pass

@admin.register(tags)
class TagAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    pass

@admin.register(ethnicity)
class EthnicityAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    pass

@admin.register(politics)
class PoliticsAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    pass

@admin.register(religious)
class ReligiousAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    pass

@admin.register(zodiacSign)
class zodiacSignAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    pass


@admin.register(family)
class FamilyAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    pass
