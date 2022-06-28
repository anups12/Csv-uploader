from django.contrib import admin
from . models import Csvdata, UploadCsv

# Register your models here.

@admin.register(UploadCsv)
class TaskRegister(admin.ModelAdmin):
    model = UploadCsv
    list_display= ('id',)

@admin.register(Csvdata)
class TaskRegister(admin.ModelAdmin):
    model = Csvdata
    list_display= ('id','name', 'dateadd')
