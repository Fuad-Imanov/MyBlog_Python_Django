from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('post/<str:slug>/', views.GetPost.as_view(), name='post'),
    path('category/<str:slug>/', views.PostsByCategory.as_view(), name='P_Category'),
    path('tag/<str:slug>/', views.PostsByTag.as_view(), name='tag'),
    path('search/',views.Search.as_view(),name='search')
]
