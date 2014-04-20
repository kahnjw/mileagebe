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

    def create(self, username, password):
        self.user = User(username=username)
        self.user.set_password(password)
        self.user.save()
        self.save()
