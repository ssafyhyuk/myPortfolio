from django.urls import path
from . import views

urlpatterns = [
    # 정기예금 저장
    path('deposit-products/save/', views.deposit_products_save),
    # 정기예금 전체 LIST
    path('deposit-products/', views.deposit_products),
    # 정기예금 상품 DETAIL
    path('deposit-products/detail/<str:fin_prdt_cd>/', views.deposit_products_detail),
    # 정기예금 옵션 DETAIL
    path('deposit-products/options/<str:fin_prdt_cd>/', views.deposit_products_options),
    # 정기예금 가입
    path('deposit-products/join/<str:fin_prdt_cd>/', views.deposit_products_join),
    # 정기예금 해지
    path('deposit-products/remove/<str:fin_prdt_cd>/', views.deposit_products_remove),

    # 적금 저장
    path('saving-products/save/', views.saving_products_save),
    # 적금 전체 LIST
    path('saving-products/', views.saving_products),
    # 적금 상품 DETAIL
    path('saving-products/detail/<str:fin_prdt_cd>/', views.saving_products_detail),
    # 적금 옵션 DETAIL
    path('saving-products/options/<str:fin_prdt_cd>/', views.saving_products_options),
    # 적금 가입
    path('saving-products/join/<str:fin_prdt_cd>/', views.saving_products_join),
    # 적금 해지
    path('saving-products/remove/<str:fin_prdt_cd>/', views.saving_products_remove),

    # 상품 추천
    path('products-recommend/', views.products_recommend),
]
