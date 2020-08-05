from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    image = models.URLField(max_length=350)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=200)
    join_date = models.DateField(auto_now=False, auto_now_add=True)
    image = models.URLField(max_length=350, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')


class Post(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    blurb = models.TextField(max_length=500)
    post_date = models.DateField(auto_now=False, auto_now_add=True)
    edit_date = models.DateField(auto_now=True)