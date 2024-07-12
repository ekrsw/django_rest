from rest_framework import serializers
from blog.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
