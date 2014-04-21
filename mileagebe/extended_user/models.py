from django.db import models
from django.contrib.auth.models import User


class ExtendedUser(models.Model):
    access_token = models.CharField(max_length=400, blank=True, null=True)
    user = models.OneToOneField(
        User, related_name='extended_user', blank=True, null=True)

    @property
    def username(self):
        try:
            return self.user.username
        except:
            return None

    @username.setter
    def username(self, value):
        self.user.username = value
        self.user.save()

    @property
    def password(self):
        try:
            return self.user.password
        except:
            return None

    @password.setter
    def password(self, value):
        self.user.password = value
        self.user.save()

    @classmethod
    def create(cls, username, password):
        extended_user = cls()
        extended_user.user = User.objects.create_user(
            username, password=password)
        extended_user.user.set_password(password)
        extended_user.user.save()
        extended_user.save()
        return extended_user
