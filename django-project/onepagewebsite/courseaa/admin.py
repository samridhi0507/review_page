from django.contrib import admin
from courseaa.models import courseaa
class courseaaAdmin(admin.ModelAdmin):
    list_display=('name','email','password')

admin.site.register(courseaa,courseaaAdmin)

# Register your models here.
