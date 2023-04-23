from django.contrib import admin
from mcq import models

admin.site.register(models.Question)
admin.site.register(models.Option)

# Register your models here.
