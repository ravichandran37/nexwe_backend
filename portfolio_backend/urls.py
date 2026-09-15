from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def root_health_check(request):
    return JsonResponse({
        "status": "online",
        "message": "Nexwe Backend API is running successfully!",
        "endpoints": {
            "projects": "/api/portfolio/projects/",
            "skills": "/api/portfolio/skills/",
            "contact": "/api/contact/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    path('', root_health_check, name='root-health-check'),
    path('admin/', admin.site.urls),
    path('api/', include('contact.urls')),
    path('api/portfolio/', include('portfolio.urls')),
]

