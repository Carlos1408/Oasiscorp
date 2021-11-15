from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, birth_date, phone, address,
            email, password = None):
        user = self.model(
                first_name = first_name,
                last_name = last_name,
                birth_date = birth_date,
                phone = phone,
                address = address,
                email = self.normalize_email(email),
                )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, birth_date, phone, address,
            email, password):
        user = self.create_user(first_name, last_name, birth_date, phone, address,
                email, password)
        user.admin = True
        user.save()


class User(AbstractBaseUser):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    birth_date = models.DateField()
    phone = models.BigIntegerField()
    address = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50, unique = True)

    active = models.BooleanField(default = True)
    admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
            'first_name', 'last_name', 'birth_date',
            'phone', 'address'
            ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin
