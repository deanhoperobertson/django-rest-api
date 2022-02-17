from rest_framwork import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ("id", "name", "language", "price")

