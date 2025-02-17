from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectListCreateView, ProjectDetailView, UserProjectsView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('user/projects/', UserProjectsView.as_view(), name='user-projects'),
]
