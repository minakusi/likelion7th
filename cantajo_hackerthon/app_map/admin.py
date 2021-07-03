from django.contrib import admin

# Register your models here.
from .models import Catlist
from .models import Catphoto

admin.site.register(Catlist)
admin.site.register(Catphoto)