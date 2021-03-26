from rest_framework import serializers
from library.models import Category, Book, StudentBorrowedBook, Section, StudentLibraryAttendance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class BookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    class Meta:
        model = Book
        fields = ('id', 'name', 'category')

class StudentBorrowedBookSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(slug_field='name', queryset=Book.objects.all())
    class Meta:
        model = StudentBorrowedBook
        fields = ('id', 'first_name', 'last_name', 'book', 'date_borrowed')

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'level', 'name')

class StudentLibraryAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLibraryAttendance
        fields = ('id', 'first_name', 'last_name', 'attendance_date','section')
        depth = 1
