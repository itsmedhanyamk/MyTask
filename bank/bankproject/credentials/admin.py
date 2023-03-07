from django.contrib import admin
from . models import District,Branches,User_details

# Register your models here.
admin.site.register(District)
admin.site.register(Branches)
admin.site.register(User_details)