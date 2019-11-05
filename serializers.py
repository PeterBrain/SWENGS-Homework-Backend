from . import models

from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ['id', 'name', 'description']
