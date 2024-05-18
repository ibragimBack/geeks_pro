from django.urls import path
from .views import TaksListAPIView, TaskDetailAPIView

urlpatterns = [
    path('', TaksListAPIView.as_view()),
    path('<int:id>/', TaskDetailAPIView.as_view()),
]