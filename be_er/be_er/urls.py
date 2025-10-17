# be_er/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from categories.views import CategoryViewSet
from posts.views import PostViewSet
from comments.views import CommentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from posts.urls import router as posts_router
from comments.urls import router as comments_router


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(posts_router.urls)),
    path('api/', include(comments_router.urls)),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
