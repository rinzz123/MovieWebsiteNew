from django.contrib import admin

from reviewapp.models import Review


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['comments','rating','movie','user']
admin.site.register(Review,ReviewAdmin)