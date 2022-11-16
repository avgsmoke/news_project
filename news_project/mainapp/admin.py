from django.contrib import admin

from mainapp.models import News, Comments, Favorite

admin.site.register(News)
admin.site.register(Comments)
admin.site.register(Favorite)
