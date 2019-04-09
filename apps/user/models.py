from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

# Create your models here.


class User(AbstractUser, BaseModel):
    '''用户'''

    class Meta:
        db_table = 'blog_user'
