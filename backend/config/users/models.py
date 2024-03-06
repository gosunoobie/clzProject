
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserCustomManager
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from core.models import SoftDeleteModel, TimeStampedModel, SingletonModel
from django.core.validators import MinLengthValidator
from core.validators import validate_file_size
from django.utils import timezone

# Create your models here.

class User(AbstractUser,SoftDeleteModel):
    """
    Main User Auth model that expand django's default User model
    """

    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(_("email address"), unique=True,validators=[MinLengthValidator(3)])
    mobile_number = models.CharField(
        null=True,
        blank=True,
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^([\s\d]+)$", message="Phone number must contain only number."
            )
        ],
    )
    avatar = models.ImageField(
        "Image",
        upload_to="avatar",
        null=True,
        blank=True,
        validators=[validate_file_size],
    )
    account_provider = models.CharField( max_length=50,default="CloudCruise")
    total_reward_coin = models.DecimalField( max_digits=15, decimal_places=2,default=0) 
    nationality = models.CharField(max_length=100,blank=True,null=True)

    # verification fields
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    phone_otp = models.CharField(max_length=6, blank=True, null=True,editable=False)
    phone_time = models.DateTimeField(blank=True, null=True,editable=False)

    reset_password_otp = models.CharField(max_length=6, blank=True, null=True,editable=False)
    reset_password_time = models.DateTimeField(blank=True, null=True,editable=False)

    email_otp = models.CharField(max_length=6, blank=True, null=True,editable=False)




    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserCustomManager()

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name_plural = "Users"

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        self.username = self.username.lower()
        return super(User, self).save(*args, **kwargs)

    def get_roles_name(self):
        return ",".join([x.name for x in self.groups.all()])
    
    def soft_delete(self, *args, **kwargs):
        """
        Soft delete the model instance.
        """
        if not self.is_deleted:            
            self.email=f"{self.id}-deleted-{self.email}"
            self.username=f"{self.id}-deleted-{self.username}"
            self.is_deleted = True
            self.is_active =False
            self.deleted_date = timezone.now()

            return super().save(*args, **kwargs)

class BankDetail(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="User having this account",
        on_delete=models.CASCADE,
    )
    priority = models.IntegerField(_("Priority"))
    account_number = models.CharField(_("Account Number"), max_length=50)
    account_holder_name = models.CharField(_("Account Holder Name"), max_length=50)
    bank_name = models.CharField(_("Bank Name"), max_length=50)

    def __str__(self):
        return f"{self.account_holder_name} - {self.bank_name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "priority"],
                name="bank_priority_constraint",
            ),
             models.UniqueConstraint(
                fields=["user",  "account_number"],
                name="bank_number_constraint",
            )
        ]
    


class Wallet(models.Model):
    name = models.CharField(_("Name of Wallet"), max_length=50)
    photo = models.ImageField(
        upload_to="wallet_photo",
        validators=[validate_file_size],
    )

    def __str__(self):
        return self.name




class PaymentWallet(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="User having this Wallet",
        on_delete=models.CASCADE,
    )
    priority = models.IntegerField(_("Priority"))
    wallet_id = models.CharField(_("Wallet Id"), max_length=50)
    wallet_holder_name = models.CharField(_("Wallet Holder name"), max_length=50)
    wallet_name = models.ForeignKey(
        Wallet,
        verbose_name="Available Wallet",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.wallet_holder_name} - {self.wallet_name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "priority"],
                name="wallet_priority_constraint",
            ),
             models.UniqueConstraint(
                fields=["user",  "wallet_id"],
                name="wallet_id_constraint",
            )
        ]


class MasterOTP(SingletonModel,TimeStampedModel):
    otp = models.CharField(max_length=6)
    
    def __str__(self):
        return self.otp
