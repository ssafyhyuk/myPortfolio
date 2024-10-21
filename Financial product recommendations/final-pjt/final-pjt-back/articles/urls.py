from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('detail/<int:article_pk>/', views.article_detail),
    path('like/<int:article_pk>/', views.article_like),

    path('comments/<int:article_pk>/', views.comment_list),
    path('comments/<int:article_pk>/<int:comment_pk>/', views.comment_detail),
    path('comments/<int:article_pk>/create/', views.comment_create),
]
