from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','email','phone')
    list_editable = ('email','phone')
    list_per_page = 8
    search_fields = ('name','gender','email','phone','info') 
    
admin.site.register(Contact,ContactAdmin)

