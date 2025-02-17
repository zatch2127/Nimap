from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Client, Project
from rest_framework import serializers  # ✅ Add this line

from .serializers import ClientSerializer, ProjectSerializer, UserSerializer

# List all clients or create a new client
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Retrieve, update, or delete a specific client
class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

# List all projects or create a new project
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        client_id = self.request.data.get('client')  # ✅ Ensure client ID is received
        if not client_id:
            raise serializers.ValidationError({"client": "This field is required."})

        try:
            client = Client.objects.get(id=client_id)  # ✅ Ensure client exists
        except Client.DoesNotExist:
            raise serializers.ValidationError({"client": "Client does not exist."})

        serializer.save(client=client, created_by=self.request.user)  # ✅ Assign client properly

  # ✅ Assign client properly
 # Assign logged-in user

# Retrieve, update, or delete a specific project
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

# List projects assigned to the logged-in user
class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)
