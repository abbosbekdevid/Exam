from django.db import models
from datetime import datetime as datenow

# Create your models here.

class AuthorModel(models.Model):
    name = models.CharField(max_length=65, default='')
    fname = models.CharField(max_length=75, default='')
    date_birth = models.DateField(default=datenow.now)
    country = models.CharField(max_length=35,default='')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'Author'


class BookCategoryModel(models.Model):
    name = models.CharField(max_length=30,default='')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'Category_book'



class BookModel(models.Model):
    title = models.CharField(max_length=120, default='')
    page = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category = models.ForeignKey(BookCategoryModel,null=True, on_delete=models.SET_NULL)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'Book'





