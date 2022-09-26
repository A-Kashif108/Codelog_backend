from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('blogs/', views.BlogList.as_view(), name='blogs'),
    path('blogs/post/', views.AddBlog.as_view(), name='blogs_add'),
    path('blogs/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('', views.getRoutes)
]