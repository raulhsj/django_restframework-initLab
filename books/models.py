from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    bookName = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publishedDate = models.DateTimeField()
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.bookName} - {self.writer}'


class Comment(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comments")
    # owner = models.CharField(max_length=255)
    # Admin or staff users
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book} - {self.comment}'
