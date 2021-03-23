from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import UserManager
import datetime
from django.conf import settings
from django.conf.urls.static import static


# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, date_of_birth, password, **extra_fields):
        if not username:
            raise ValueError(_('A username must be provided'))
        if not email:
            raise ValueError(_('An email must be provided'))
        if not date_of_birth:
            raise ValueError(_('A date of birth must be provided: YYYY-mm-dd'))

        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, date_of_birth, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must be assigned is_active=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned is_superuser=True')

        return self.create_user(username, email, date_of_birth, password, **extra_fields)

# class CustomUserManager(BaseUserManager):
#     use_in_migrations = True

#     def create_base_user(self, username, email, date_of_birth, password, **extra_fields):

#         if not username:
#             raise ValueError(_('An username must be provided'))
#         if not email:
#             raise ValueError(_('An email address must be provided'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_user(self, username, email, date_of_birth, password, **extra_fields):
#         extra_fields.setdefault('is_active', False)
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self.create_base_user(username, email, password, **extra_fields)

#     def create_superuser(self, username, email, date_of_birth, password, **extra_fields):

#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')

#         return self.create_base_user(username, email, date_of_birth, password, **extra_fields)


def user_icon_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'icons/{0}/'.format(filename)


def user_banner_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'banners/{0}/'.format(filename)


def generate_unique_code():
    length = 8

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        # ChatRoom.objects accesses all class objects
        if ChatRoom.objects.filter(code=code).count() == 0:
            break

    return code


class UserProfile(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        verbose_name='username',
        max_length=25,
        unique=True,
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
    )

    date_of_birth = models.DateField(
        _('Date of birth'),
    )

    date_joined = models.DateTimeField(
        _('Date joined'),
        default=timezone.now,
    )

    user_bio = models.CharField(
        _('User Bio'),
        max_length=300,
        default='',
        blank=True,
    )

    user_icon = models.ImageField(
        _('User icon'),
        upload_to=user_icon_path,
        default='default_user.png',
    )

    is_hosting = models.BooleanField(default=False)  # hosting a chatroom
    is_online = models.BooleanField(default=False)

    # Django default user fields
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)  # activated i.e. verified
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'date_of_birth']

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        #db_table = 'auth_user'
        abstract = False

    def get_profile_url(self):
        return "/users/%i/" % (self.username)

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def __str__(self):
        return self.username


class UserFollow(models.Model):
    user_following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='Following',
        on_delete=models.CASCADE,
    )

    user_followers = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='Followers',
        on_delete=models.CASCADE,
    )

    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_following', 'user_followers')


class UserModding(models.Model):
    mod_for = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='mod_for',
        on_delete=models.CASCADE,
    )

    my_mods = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='my_mods',
        on_delete=models.CASCADE,
    )

    modded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('mod_for', 'my_mods')


class UserBlock(models.Model):
    block_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='ban_user',
        on_delete=models.CASCADE,
    )

    blocked_from = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='ban_from',
        on_delete=models.CASCADE,
    )

    blocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('block_user', 'blocked_from')


class ChatRoom(models.Model):

    # Max number of people in chat
    max_chat = models.IntegerField(
        max_length=None,
    )

    # Number of people
    num_chat = models.IntegerField(
        default=1,
    )

    # code to enter a room
    chat_code = models.CharField(
        max_length=8,
        default=generate_unique_code,
        unique=True,
    )

    # By default the chat is open to anyone
    open_chat = models.BooleanField(
        default=True,
    )

    # Get the time when room was created
    live_at = models.DateTimeField(
        auto_now_add=True,
    )
