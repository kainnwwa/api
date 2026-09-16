from django.urls import path
from .views import ViewTask, ViewTag, ViewTaskTag   

urlpatterns = [
    path('tasks/', ViewTask.as_view()),
    path('tags/', ViewTag.as_view()),
    path('task-tags/', ViewTaskTag.as_view()),
]