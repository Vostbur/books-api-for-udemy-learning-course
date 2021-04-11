from django.db import models


class Isbn(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return f'{self.isbn_10} {self.isbn_13}'


class Book(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=500, blank=True)
    published = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='img', blank=True, null=True)

    isbn = models.OneToOneField(Isbn, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Character(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    book = models.ManyToManyField(Book, related_name='authors')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
