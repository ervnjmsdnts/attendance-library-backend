from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from attendance.models import Section, StudentAttendance
from attendance.serializers import SectionSerializer, StudentAttendanceSerializer
# Create your views here.

class SectionView(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class StudentAttendanceView(viewsets.ModelViewSet):
    queryset = StudentAttendance.objects.all().order_by('-id')
    serializer_class = StudentAttendanceSerializer

    def create(self, request, *args, **kwargs):
        student_data = request.data

        new_student = StudentAttendance.objects.create(
            first_name = student_data['first_name'],
            last_name = student_data['last_name'],
            section = Section.objects.get(name=student_data['section']),
        )

        new_student.save()
        serializer = StudentAttendanceSerializer(new_student)

        return Response(serializer.data)
