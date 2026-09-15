from rest_framework import generics
from .models import Project, Skill
from .serializers import ProjectSerializer, SkillSerializer

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
