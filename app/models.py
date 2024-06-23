import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_year = models.IntegerField(default=datetime.date.today().year)
    summary = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    score = models.IntegerField(default=0,   validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ], null= True)
    review_text =  models.CharField(max_length=500, null= True)

    def __str__(self):
        return self.book.title + " review " + str(self.id) 