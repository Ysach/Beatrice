from django.contrib import admin

import custom_user_admin
# Register your models here.
import models

admin.site.register(models.UserProfile, custom_user_admin.UserProfileAdmin)
admin.site.register(models.PhotoUpload)
