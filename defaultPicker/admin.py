from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


@admin.register(age)
class AgeAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    pass

@admin.register(tags)
class TagAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    list_display = ['id', 'tag', 'tag_fr']
    search_fields = ['id', 'tag', 'tag_fr']

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

@admin.register(interestedIn)
class InterestedInAdmin(ImportExportModelAdmin, ExportActionMixin,admin.ModelAdmin):
    list_display = ['id', 'interest', 'interest_fr']
