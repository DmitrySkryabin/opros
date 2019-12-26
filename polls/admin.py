from django.contrib import admin

from .models import *

admin.site.register(Question_group)
admin.site.register(Question)
admin.site.register(Choice)
