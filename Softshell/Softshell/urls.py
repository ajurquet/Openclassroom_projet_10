from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter, DefaultRouter
from Project.views import ProjectViewSet
from Issue.views import IssueViewSet
from User.views import ContributorViewSet, UserViewSet
from Comment.views import CommentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_nested import routers


router = SimpleRouter()
router.register(r'projects', ProjectViewSet)

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
users_router = routers.NestedSimpleRouter(router, r'projects', lookup='user')

projects_router.register(r'issues', IssueViewSet)
projects_router.register(r'users', ContributorViewSet)

issues_router = routers.NestedSimpleRouter(projects_router, r'issues', lookup='issue')
issues_router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls)),
    path('', include(users_router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('signup/', UserViewSet.as_view({'post': 'create'}), name='signup')
    # path('signup/', include('rest_auth.registration.urls')),
]