"""Softshell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Projects.views import ProjectsViewSet
from Issues.views import IssuesViewSet
# from Comments import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'projects', ProjectsViewSet)
router.register(r'issues', IssuesViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]




# from django.conf.urls import include
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('projects/', include('Projects.urls')),
# ]

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]