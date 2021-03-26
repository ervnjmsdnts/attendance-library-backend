from rest_framework import serializers
from attendance.models import Section, StudentAttendance

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'level', 'name')

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = ('id', 'first_name', 'last_name', 'attendance_date','section')
        depth = 1