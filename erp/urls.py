from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, AuthorViewSet, ArticleViewSet, CommentViewSet, index

# Routerni yaratamiz va kerakli viewsetlarni ro'yxatdan o'tkazamiz
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  
    path('', index, name='index'),     
]
