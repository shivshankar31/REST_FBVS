from dataclasses import fields
from rest_framework import serializers
from fbvapp.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['Id', 'Name', 'Mark', 'Location']

        