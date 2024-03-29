from django.contrib import admin
from .models import Category,Movie
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','slug','poster','description','release_date','actors','category','link']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Movie,MovieAdmin)
