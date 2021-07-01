from rest_framework import serializers
from .models import EditSQL

class EditSQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditSQL
        fields = ['input_text']