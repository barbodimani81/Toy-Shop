from django.urls import path, include

from rest_framework import routers

from .views import CategoryViewSet, ProductViewSet, CommentViewSet, ImageViewSet, VideoViewSet

# category urls
category_router = routers.DefaultRouter()
category_router.register('', CategoryViewSet, )

# product urls
product_router = routers.DefaultRouter()
product_router.register('', ProductViewSet, )

# comment urls
comment_router = routers.DefaultRouter()
comment_router.register('', CommentViewSet, )

# Image urls
image_router = routers.DefaultRouter()
image_router.register('', ImageViewSet),

# video urls
video_router = routers.DefaultRouter()
video_router.register('', VideoViewSet)

urlpatterns = [
    path('categories/', include(category_router.urls, ), ),
    path('products/', include(product_router.urls, ), ),
    path('comments/', include(comment_router.urls, ), ),
    path('image/', include(image_router.urls, ), ),
    path('video/', include(video_router.urls, ), ),
]
