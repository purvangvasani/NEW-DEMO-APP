# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from random import choices
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Technology(models.Model):
    id = models.AutoField(primary_key=True)
    techName = models.CharField(max_length=200)
    techSubname = models.CharField(max_length=10)
    description = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "Technology"


def __str__(self):
    return self.techName


Experience = [
    {'fresher', 'Fresher'},
    {'intermediate', 'Intermediate'},
    {'professional', 'Professional'},
]

class Questions(models.Model):
    qid = models.AutoField(primary_key=True)
    question = RichTextField(blank=True, null=True)
    answer = RichTextField(blank=True, null=True)
    experience = models.CharField(max_length=300, choices=Experience, null=True)
    technology = models.ForeignKey(
        Technology, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "Questions"