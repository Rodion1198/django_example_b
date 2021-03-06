import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField("email")
    password = models.CharField(max_length=200)

    def __str__(self):
        return f'Name: {self.username} Email: {self.email} Password: {self.password}'


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField("emails")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"


class Logg(models.Model):
    path = models.CharField(max_length=20)
    method = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.path}, {self.method}, {self.timestamp}"
