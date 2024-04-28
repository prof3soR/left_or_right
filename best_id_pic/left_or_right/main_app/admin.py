from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.votes)
admin.site.register(models.feedback)
