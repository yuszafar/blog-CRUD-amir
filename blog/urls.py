from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    path('create/', views.PostCreate.as_view()),
    path('list/', views.PostList.as_view()),
    path('<int:post_id>/', include([
        path('', views.PostDetail.as_view()),
        path('comment/', include([
            path('create/', views.CommentCreate.as_view()),
            path('list/', views.CommentList.as_view()),
            path('<int:comment_id>/', views.CommentDetail.as_view()),
        ])),
    ])),
]
