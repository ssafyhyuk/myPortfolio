from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter

import random

def image_url():
    c = str(random.randrange(1, 16))
    if c in ['1', '2']:
        return c + '.gif'
    else:
        return c + '.png'


class User(AbstractUser):
    age = models.IntegerField()
    asset = models.TextField()
    income = models.TextField()
    nickname = models.TextField()

    image = models.ImageField(null=True, blank=True, default='profile/default/' + image_url(), upload_to="profile/user/")

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        age = data.get("age")
        asset = data.get("asset")
        income = data.get("income")
        nickname = data.get("nickname")

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if age:
            # user_field(user, "age", age)
            user.age = age
        if asset:
            user_field(user, "asset", asset)
        if income:
            user_field(user, "income", income)
        if nickname:
            user_field(user, "nickname", nickname)

        user.image = data.get("image") if data.get("image") else user.image



        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user
