
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.query import QuerySet
from django.contrib.auth.models import Group
from django.utils import timezone



class UserSoftDeleteQuerySet(QuerySet):
    def only_deleted(self):
        return self.filter(is_deleted=True)

    def not_deleted(self):
        return self.filter(is_deleted=False)

    def soft_delete(self):
        # print("soft delete user is working")
        return self.update(
               
                is_deleted=True,
                deleted_date=timezone.now()
            )

    def restore(self):
        return self.update(is_deleted=False, deleted_date=None)

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """


    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        admin,_ = Group.objects.get_or_create(name="Admin")
        user = self.create_user(email, password, **extra_fields)
        user.groups.add(admin)
        return user
    
    def get_queryset(self):
        return self.queryset(self.model, using=self._db).not_deleted()
    
    def only_deleted(self):
        return self.queryset(self.model, using=self._db).only_deleted()

    def with_deleted(self):
        return self.queryset(self.model, using=self._db)
    
class UserCustomManager(CustomUserManager):
    queryset = UserSoftDeleteQuerySet
