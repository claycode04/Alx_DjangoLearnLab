
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet, CommentViewSet
from .feed import Feed

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls + [
	# Feed endpoint
	path('feed/', Feed.as_view(), name='feed'),
]
