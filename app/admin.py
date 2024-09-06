from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile , Tweet

# Unregister Group from admin site
admin.site.unregister(Group)



# mix profile into user infomation 
class ProfileInline(admin.StackedInline):
    model=Profile


# Extend User model
class UserAdmin(admin.ModelAdmin):  
    model = User
    # the username field in the admin page
    fields = ["username"]
    inlines = [ProfileInline]



# Unregister and re-register User with the extended UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)  #  registration with UserAdmin
# admin.site.register(Profile)

admin.site.register(Tweet) 



