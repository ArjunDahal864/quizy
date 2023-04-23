from django.contrib import admin
from course import models

admin.site.register(models.Course)
admin.site.register(models.Semester)
admin.site.register(models.Subject)