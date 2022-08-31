from django.contrib import admin
from .models import RegType, SupportGroup, LocalGovt, Team, Profile, Gender

admin.site.register([RegType,SupportGroup,LocalGovt, Profile, Gender,Team])