from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkAssignmentAPIView, ProjectViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="projects")

urlpatterns = [
    
    path("work_assignment/list/<int:employee_id>/", WorkAssignmentAPIView.as_view(), name="work_assignment_list"),
    path("work_assignment/create/", WorkAssignmentAPIView.as_view(), name="work_assignment_create"),
    path("work_assignment/update/<int:pk>/", WorkAssignmentAPIView.as_view(), name="work_assignment_update"),
    path("work_assignment/delete/<int:pk>/", WorkAssignmentAPIView.as_view(), name="work_assignment_delete"),

    
    path("", include(router.urls)),
]