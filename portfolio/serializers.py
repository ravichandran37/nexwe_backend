from rest_framework import serializers
from .models import Project, Skill

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def to_representation(self, instance):
        """Format to match exactly what the React frontend expects"""
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'title': data['title'],
            'description': data['description'],
            'badges': data['badges'],
            'features': data['features'],
            'architectureSteps': data['architecture_steps'],
            'caseStudy': {
                'overview': data['case_study_overview'],
                'problem': data['case_study_problem'],
                'solution': data['case_study_solution'],
                'features': data['case_study_features'],
                'architecture': data['case_study_architecture'],
                'technologies': data['case_study_technologies'],
                'challenges': data['case_study_challenges'],
                'result': data['case_study_result'],
            }
        }

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'category', 'icon', 'items']
