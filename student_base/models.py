from __future__ import unicode_literals

from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=20)
    starosta = models.ForeignKey('Student', blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    birth_day = models.DateField()
    ticket_number = models.IntegerField()
    group_names = models.ForeignKey('Group')

    def __str__(self):
        return self.name








