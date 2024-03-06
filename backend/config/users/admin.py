from django.contrib import admin
from .models import User,  BankDetail, PaymentWallet, Wallet 
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from core.admin import ShowWithDeletedAdmin


class CustomUserAdmin(UserAdmin,ShowWithDeletedAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "id",
        "username",
        "email",
        "is_active",
        "mobile_number",
        "get_roles_name",
        "account_provider",
        "is_deleted"
    ]
    list_filter = ("email", "is_staff", "is_active", "account_provider")
    fieldsets = (
        (
            "General Data",
            {
                "fields": (
                    "username",
                    "email",
                    "mobile_number",
                    "first_name",
                    "last_name",
                    "avatar",
                    "nationality",
                    "password",
                    "account_provider",
                    "total_reward_coin",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "is_deleted",
                    "deleted_date",
                    "phone_verified",
                    "email_verified",
                )
            },
        ),
        (
            "OTP Related ",
            {
                "fields": (
                    "phone_otp",
                    "reset_password_otp",
                    "email_otp",
                    "reset_password_time",
                )
            },
        ),
        ("Assign Group ", {"fields": ("groups",)}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("-id",)
    readonly_fields = (
        "phone_otp",
        "last_login",
        "email_otp",
        "reset_password_otp",
        "reset_password_time",
        "deleted_date",
        "total_reward_coin"
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(BankDetail)
admin.site.register(Wallet)
admin.site.register(PaymentWallet)
