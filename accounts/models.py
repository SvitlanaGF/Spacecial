from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.


class UserModel(auth_models.User, auth_models.PermissionsMixin):

    def __str__(self):
        return f'@{self.username}'


