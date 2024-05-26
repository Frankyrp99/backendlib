from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

# Create your models here


class UserManager(BaseUserManager):
    def create_user(self, nombre,apellidos,email, password, **extra_fields):
        if not email:
            raise ValueError('Falta el Email')
        user = self.model(nombre=nombre,apellidos=apellidos, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, nombre,apellidos, email, password):
        user = self.create_user(nombre,apellidos,email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_ROLES = (
        ('admin', 'Administrador'),
        ('especialista', 'Especialista'),
        ('invitado', 'Invitado'),
    )
    
    nombre=models.CharField( max_length=50)
    apellidos=models.CharField( max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='invitado')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.nombre