from django.contrib import admin
from .models import Chats,CreateTopic,Department,Replies
# Register your models here.

admin.site.register(Chats)
admin.site.register(Replies)
admin.site.register(Department)
admin.site.register(CreateTopic)