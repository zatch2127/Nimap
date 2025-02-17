from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Client
        fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())  # ✅ Accepts client ID
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())  # ✅ Accepts user IDs
    created_by = serializers.ReadOnlyField(source='created_by.username')
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
