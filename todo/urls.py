from django.urls import path
from .views import TaskListCreateView,TaskDetailView



urlpatterns = [
    path('task/', TaskListCreateView.as_view(),name="task-create"),
    path('task/<int:pk>/',TaskDetailView.as_view(),name='task-details')
    
]
