from django.urls import path
from .views import ProjectListView, SkillListView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('skills/', SkillListView.as_view(), name='skill-list'),
]
