from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from library.models import Category, Book, StudentBorrowedBook, StudentLibraryAttendance, Section
from library.serializers import CategorySerializer, BookSerializer, StudentBorrowedBookSerializer, StudentLibraryAttendanceSerializer, SectionSerializer
# Create your views here.

class StudentBorrowedBookView(viewsets.ModelViewSet):
    queryset = StudentBorrowedBook.objects.all()
    serializer_class = StudentBorrowedBookSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SectionView(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class StudentLibraryAttendanceView(viewsets.ModelViewSet):
    queryset = StudentLibraryAttendance.objects.all()
    serializer_class = StudentLibraryAttendanceSerializer

    def create(self, request, *args, **kwargs):
        student_data = request.data

        new_student = StudentLibraryAttendance.objects.create(
            first_name = student_data['first_name'],
            last_name = student_data['last_name'],
            section = Section.objects.get(name=student_data['section']),
        )

        new_student.save()
        serializer = StudentLibraryAttendanceSerializer(new_student)

        return Response(serializer.data)
