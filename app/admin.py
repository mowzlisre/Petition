from django.contrib import admin
from .models import User, Petition

admin.site.register(Petition)
admin.site.register(User)
