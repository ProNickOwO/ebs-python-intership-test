from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, BlogItemPost, BlogItemComment
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'comment', BlogItemComment, basename='comment')
router.register(r'post', BlogItemPost, basename='post')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
]
