from django.urls import path
from . import views

urlpatterns = [
    # 환율 저장
    path('save/', views.exchanges_save),
    # 환율 정보
    path('', views.exchanges),
]
