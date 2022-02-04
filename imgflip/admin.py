from django.contrib import admin
from imgflip.models import MemeModel

## register memes to be availabe in admin panel
admin.site.register(MemeModel)
