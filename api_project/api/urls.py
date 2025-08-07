from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import UserViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
router.register(r'user_all', UserViewSet, basename='user_all')


urlpatterns = [  # Maps to the BookList view
     # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('user/', UserViewSet.as_view(), name='user-list'),
 
]