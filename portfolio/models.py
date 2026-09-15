from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    badges = models.JSONField(default=list, help_text="List of strings e.g. ['Python', 'Django']")
    features = models.JSONField(default=list)
    architecture_steps = models.JSONField(default=list)
    
    # Case Study Fields
    case_study_overview = models.TextField(blank=True)
    case_study_problem = models.TextField(blank=True)
    case_study_solution = models.TextField(blank=True)
    case_study_features = models.TextField(blank=True)
    case_study_architecture = models.TextField(blank=True)
    case_study_technologies = models.TextField(blank=True)
    case_study_challenges = models.TextField(blank=True)
    case_study_result = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    category = models.CharField(max_length=255)
    icon = models.CharField(max_length=50, help_text="Lucide React icon name, e.g., 'Layout'")
    items = models.JSONField(default=list, help_text="List of strings e.g. ['React', 'JS']")

    def __str__(self):
        return self.category
