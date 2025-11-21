from django.contrib import admin
from .models import UserInfo, DemoModel
# Register your models here.

admin.site.register([DemoModel, UserInfo])
