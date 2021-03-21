from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings

# Create your models here.


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


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        max_length=25,
        unique=True,
    )

    email = models.EmailField(
        unique=True,
    )

    date_of_birth = models.DateField()

    date_joined = models.DateField(default=timezone.now)

    user_bio = models.CharField(
        max_length=300,
        default='',
        blank=True,
    )

    user_icon = models.ImageField(
        upload_to=user_directory_path,
        default='default_user.png',
    )

    is_active = models.BooleanField(
        default=False,
    )

    is_hosting = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth']

    def __str__(self):
        return self.username


class UserFollow(models.Model):
    user_following = models.ForeignKey(
        UserProfile,
        related_name='Following',
        on_delete=models.CASCADE,
    )

    user_followers = models.ForeignKey(
        UserProfile,
        related_name='Followers',
        on_delete=models.CASCADE,
    )

    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_following', 'user_followers')


class UserModding(models.Model):
    mod_for = models.ForeignKey(
        UserProfile,
        related_name='mod_for',
        on_delete=models.CASCADE,
    )

    my_mods = models.ForeignKey(
        UserProfile,
        related_name='my_mods',
        on_delete=models.CASCADE,
    )

    modded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('mod_for', 'my_mods')


class UserBlock(models.Model):
    block_user = models.ForeignKey(
        UserProfile,
        related_name='ban_user',
        on_delete=models.CASCADE,
    )

    blocked_from = models.ForeignKey(
        UserProfile,
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
