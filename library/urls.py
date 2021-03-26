from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import StudentBorrowedBookView, CategoryView, BookView, SectionView, StudentLibraryAttendanceView

router = DefaultRouter()

router.register('student_borrowed_book', StudentBorrowedBookView, basename='student_borrowed_book')
router.register('category', CategoryView, basename='category')
router.register('book', BookView, basename='book')
router.register('section', SectionView, basename='section')
router.register('student_library_attendance', StudentLibraryAttendanceView, basename='student_library_attendance')

urlpatterns = [
    path('', include(router.urls)),
]
