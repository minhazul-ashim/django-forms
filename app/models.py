from django.db import models

# Create your models here.
class Book(models.Model) :
    authorName = models.CharField(max_length = 200);
    id = models.IntegerField(primary_key = True);
    pages = models.IntegerField(max_length = 200);
    coAuthor = models.CharField(max_length = 200);
    authorIntro = models.CharField(max_length = 200);
    bookIntro = models.CharField(max_length = 200);
    published = models.DateField(max_length = 200);
    reviewed = models.DateField(max_length = 200);
    notes = models.CharField(max_length = 200);