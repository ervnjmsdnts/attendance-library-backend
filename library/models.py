from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudentBorrowedBook(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_borrowed = models.DateTimeField(auto_now_add=True)

class Section(models.Model):
    level = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StudentLibraryAttendance(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    attendance_date = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

