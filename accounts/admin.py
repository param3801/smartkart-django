from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,UserProfile
from django.utils.html import format_html
class YourCustomModelAdmin(admin.ModelAdmin):
      list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined','last_login', 'is_active')
      search_fields = ('email', 'username', 'first_name', 'last_name')
      readonly_fields = ('date_joined', 'last_login','password')
      filter_horizontal = ()
      list_filter = ('is_admin', 'is_staff', 'is_active')
      fieldsets = ()
      ordering = ('-date_joined',)


# userprofile
class UserProfileAdmin(admin.ModelAdmin):
      # list_display = ('user', 'profile_picture', 'cover_photo', 'address_line_1', 'address_line_2', 'city', 'state', 'country', 'pincode', 'latitude', 'longitude')
      # set profile_picture at first
      def thumbnail(self, obj):
          if obj.profile_picture:
              return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />'.format(obj.profile_picture.url))
              return ""
      thumbnail.short_description = 'Profile Picture'

          
      list_display = ('thumbnail','user', 'city', 'state', 'country')
      search_fields = ('user__first_name', 'user__last_name', 'user__email', 'city', 'state', 'country')
      
       
admin.site.register(Account, YourCustomModelAdmin)
admin.site.register(UserProfile, UserProfileAdmin)



