# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Catalog(models.Model):
    Book_Name=models.CharField(max_length=255)
    Author_Name=models.CharField(max_length=255)
    Reader_Name=models.CharField(max_length=255)
    Category=models.CharField(max_length=255)
    Rate=models.IntegerField()
    def __str__(self):
        return self.Reader_Name+" - "+self.Book_Name
