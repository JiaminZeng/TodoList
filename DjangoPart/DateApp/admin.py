from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Plan)
admin.site.register(Daily)
admin.site.register(ChangeThings)
admin.site.register(ChangeHistory)
