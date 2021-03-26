from django.urls import path
from rest_framework.routers import DefaultRouter
from attendance.views import SectionView, StudentAttendanceView

router = DefaultRouter()
router.register('section', SectionView, basename='section')
router.register('student_attendance', StudentAttendanceView, basename='student_attendance')

urlpatterns = router.urls
