from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import UserManager
import datetime


# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        s_user_date = datetime.datetime(1900, 1, 1).strftime("%Y-%m-%d")
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('date_of_birth', s_user_date)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


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
        verbose_name='email address',
        unique=True,
    )

    date_of_birth = models.DateField(
        verbose_name='Date of birth',
    )

    date_joined = models.DateTimeField(
        verbose_name='Date joined',
        default=timezone.now,
    )

    user_bio = models.CharField(
        verbose_name='User Bio',
        max_length=300,
        default='',
        blank=True,
    )

    user_icon = models.ImageField(
        verbose_name='User icon',
        upload_to=user_directory_path,
        default='default_user.png',
    )

    is_active = models.BooleanField(default=False)  # online
    is_hosting = models.BooleanField(default=False)  # hosting a chatroom
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

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

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


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
