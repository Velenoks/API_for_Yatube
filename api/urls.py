from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'posts',
                views.PostViewSet,
                basename=app_name)
router.register(r'posts/(?P<id_post>\d+)/comments',
                views.CommentViewSet,
                basename=app_name)
router.register(r'group',
                views.GroupViewSet,
                basename=app_name)
router.register(r'follow',
                views.FollowViewSet,
                basename=app_name)

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/', include(router.urls)),
]
