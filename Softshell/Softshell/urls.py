from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from Project.views import ProjectViewSet
from Issue.views import IssueViewSet
from User.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'issue', IssueViewSet)
router.register(r'user', UserViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
