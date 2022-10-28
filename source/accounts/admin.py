# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
# from accounts.models import Account
#
#
# class AccountInline(admin.StackedInline):
#     model = Account
#     fields = ('username', 'email')
#
#
# class AccountAdmin(UserAdmin):
#     inlines = (AccountInline,)
#
#
# User = get_user_model()
# admin.site.unregister(User)
# admin.site.register(User, AccountAdmin)
