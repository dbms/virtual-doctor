from django.contrib import admin

# Register your models here.
from .models import Users, History

admin.site.register(Users)
admin.site.register(History)

