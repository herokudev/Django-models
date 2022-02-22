from django.contrib import admin

from .models import FirstModel, PersonModel

admin.site.register(FirstModel)
admin.site.register(PersonModel)