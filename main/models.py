from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    publication_date = models.DateField()
    cover_photo = models.ImageField(upload_to='book_covers/')
