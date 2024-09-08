from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, CustomTokenObtainPairView
from .views import (
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
    CartListCreateAPIView, CartRetrieveUpdateDestroyAPIView,
    BannerListCreateAPIView, BannerRetrieveUpdateDestroyAPIView,
    SideMenuListCreateAPIView, SideMenuRetrieveUpdateDestroyAPIView,
    ProductImgListCreateAPIView, ProductImgRetrieveUpdateDestroyAPIView,
    CartProductListCreateAPIView, CartProductRetrieveUpdateDestroyAPIView,
    OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView,
    ProductEnterListCreateAPIView, ProductEnterRetrieveUpdateDestroyAPIView,
    FeatureProductListCreateAPIView, FeatureProductRetrieveUpdateDestroyAPIView,
    RecentArticlesListCreateAPIView, RecentArticlesRetrieveUpdateDestroyAPIView,
    FooterBottomImgListCreateAPIView, FooterBottomImgRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    # Product URLs
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),

    # Cart URLs
    path('carts/', CartListCreateAPIView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartRetrieveUpdateDestroyAPIView.as_view(), name='cart-detail'),

    # Banner URLs
    path('banners/', BannerListCreateAPIView.as_view(), name='banner-list-create'),
    path('banners/<int:pk>/', BannerRetrieveUpdateDestroyAPIView.as_view(), name='banner-detail'),

    # SideMenu URLs
    path('sidemenu/', SideMenuListCreateAPIView.as_view(), name='sidemenu-list-create'),
    path('sidemenu/<int:pk>/', SideMenuRetrieveUpdateDestroyAPIView.as_view(), name='sidemenu-detail'),

    # ProductImg URLs
    path('product-images/', ProductImgListCreateAPIView.as_view(), name='productimg-list-create'),
    path('product-images/<int:pk>/', ProductImgRetrieveUpdateDestroyAPIView.as_view(), name='productimg-detail'),

    # CartProduct URLs
    path('cart-products/', CartProductListCreateAPIView.as_view(), name='cartproduct-list-create'),
    path('cart-products/<int:pk>/', CartProductRetrieveUpdateDestroyAPIView.as_view(), name='cartproduct-detail'),

    # Order URLs
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),

    # ProductEnter URLs
    path('product-enter/', ProductEnterListCreateAPIView.as_view(), name='productenter-list-create'),
    path('product-enter/<int:pk>/', ProductEnterRetrieveUpdateDestroyAPIView.as_view(), name='productenter-detail'),

    # FeatureProduct URLs
    path('feature-products/', FeatureProductListCreateAPIView.as_view(), name='featureproduct-list-create'),
    path('feature-products/<int:pk>/', FeatureProductRetrieveUpdateDestroyAPIView.as_view(), name='featureproduct-detail'),

    # RecentArticles URLs
    path('recent-articles/', RecentArticlesListCreateAPIView.as_view(), name='recentarticles-list-create'),
    path('recent-articles/<int:pk>/', RecentArticlesRetrieveUpdateDestroyAPIView.as_view(), name='recentarticles-detail'),

    # FooterBottomImg URLs
    path('footer-bottom-images/', FooterBottomImgListCreateAPIView.as_view(), name='footerbottomimg-list-create'),
    path('footer-bottom-images/<int:pk>/', FooterBottomImgRetrieveUpdateDestroyAPIView.as_view(), name='footerbottomimg-detail'),
    
    # docs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
