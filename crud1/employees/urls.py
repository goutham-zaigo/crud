from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkAssignmentAPIView, ProjectViewSet


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    
    path('workassignments/<int:employee_id>/', WorkAssignmentAPIView.as_view(), name='workassignments-list'),
    path('workassignments/<int:pk>/', WorkAssignmentAPIView.as_view(), name='workassignments-detail'),

    
    path('', include(router.urls)),
]
