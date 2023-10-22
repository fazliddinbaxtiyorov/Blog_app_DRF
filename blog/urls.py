from django.urls import path
from .views import All_Blogs, Blog_Create, Blog_Delete, Blog_Detail, User_Blog_Search, Blog_Update, Sorted


urlpatterns = [
    path('api/', All_Blogs.as_view()),
    path('api/new/', Blog_Create.as_view()),
    path('api/<int:pk>/', Blog_Detail.as_view()),
    path('api/<int:pk>/delete/', Blog_Delete.as_view()),
    path('api/<int:pk>/update/', Blog_Update.as_view()),
    path('api/<username>/', User_Blog_Search.as_view()),
    path('api/sort/<str:field>', Sorted.as_view())
]
