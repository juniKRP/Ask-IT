from django.db import models
from django.conf import settings


# Create your models here.
class Module(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    pub_date = models.DateTimeField(auto_now=True)
    admins = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="module_admins")
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="module_members")

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    explanation = models.CharField(max_length=3000)
    tried_what = models.CharField(max_length=500)
    summary = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default="Unanswered")
    tags = models.ManyToManyField(Tag, related_name="question_tags")
    score = models.IntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    upvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="question_upvotes")
    downvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="question_downvotes")

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=3000)
    pub_date = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    upvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="answer_upvotes")
    downvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="answer_downvotes")
    is_solution = models.BooleanField(default=False)


    def __str__(self):
        return self.content


class User(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Notifications(models.Model):
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    detail = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.detail

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.author