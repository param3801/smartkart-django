from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
class YourCustomModelAdmin(admin.ModelAdmin):
      list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined','last_login', 'is_active')
      search_fields = ('email', 'username', 'first_name', 'last_name')
      readonly_fields = ('date_joined', 'last_login','password')
      filter_horizontal = ()
      list_filter = ('is_admin', 'is_staff', 'is_active')
      fieldsets = ()
      ordering = ('-date_joined',)
       
admin.site.register(Account, YourCustomModelAdmin)



