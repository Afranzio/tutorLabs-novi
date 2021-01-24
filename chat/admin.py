from django.contrib import admin
from .models import Message 
from basic.models import User
# Register your models here.
admin.site.register(Message)
admin.site.register(User)