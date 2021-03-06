from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-  
  
  
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    redaction = models.ForeignKey('Redaction', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    book_cover = models.ImageField(upload_to='covers', blank=True)


    def __str__(self):
        return self.title


class Redaction(models.Model):
    objects = None
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Friend(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    data = models.CharField(max_length=20)

    def __str__(self):
        return self.name

