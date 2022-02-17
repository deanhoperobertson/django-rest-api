from django.shortcuts import render
from rest_framwork import viewsets
from .models import Course
from .serializers import CourseSerializer

class Courseiew(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

