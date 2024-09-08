from rest_framework import generics
from Goods.models import (
    Category, Product, Cart, Banner, SideMenu, ProductImg, CartProduct,
    Order, ProductEnter, FeatureProduct, RecentArticles, FooterBottomImg
)
from .serializers import (
    CategorySerializer, ProductSerializer, CartSerializer,
    BannerSerializer, SideMenuSerializer, ProductImgSerializer,
    CartProductSerializer, OrderSerializer, ProductEnterSerializer,
    FeatureProductSerializer, RecentArticlesSerializer,
    FooterBottomImgSerializer, CustomTokenObtainPairSerializer
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.views import TokenObtainPairView

# Category Views
@method_decorator(login_required(login_url='login'))
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@method_decorator(login_required(login_url='login'))
class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product Views
@method_decorator(login_required(login_url='login'))
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@method_decorator(login_required(login_url='login'))
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Cart Views
@method_decorator(login_required(login_url='login'))
class CartListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

@method_decorator(login_required(login_url='login'))
class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Banner Views
@method_decorator(login_required(login_url='login'))
class BannerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

@method_decorator(login_required(login_url='login'))
class BannerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

# SideMenu Views
@method_decorator(login_required(login_url='login'))
class SideMenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = SideMenu.objects.all()
    serializer_class = SideMenuSerializer

@method_decorator(login_required(login_url='login'))
class SideMenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SideMenu.objects.all()
    serializer_class = SideMenuSerializer

# ProductImg Views
@method_decorator(login_required(login_url='login'))
class ProductImgListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductImg.objects.all()
    serializer_class = ProductImgSerializer

@method_decorator(login_required(login_url='login'))
class ProductImgRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImg.objects.all()
    serializer_class = ProductImgSerializer

# CartProduct Views
@method_decorator(login_required(login_url='login'))
class CartProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

@method_decorator(login_required(login_url='login'))
class CartProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

# Order Views
@method_decorator(login_required(login_url='login'))
class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@method_decorator(login_required(login_url='login'))
class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# ProductEnter Views
@method_decorator(login_required(login_url='login'))
class ProductEnterListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductEnter.objects.all()
    serializer_class = ProductEnterSerializer

@method_decorator(login_required(login_url='login'))
class ProductEnterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductEnter.objects.all()
    serializer_class = ProductEnterSerializer

# FeatureProduct Views
@method_decorator(login_required(login_url='login'))
class FeatureProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = FeatureProduct.objects.all()
    serializer_class = FeatureProductSerializer

@method_decorator(login_required(login_url='login'))
class FeatureProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeatureProduct.objects.all()
    serializer_class = FeatureProductSerializer

# RecentArticles Views
@method_decorator(login_required(login_url='login'))
class RecentArticlesListCreateAPIView(generics.ListCreateAPIView):
    queryset = RecentArticles.objects.all()
    serializer_class = RecentArticlesSerializer

@method_decorator(login_required(login_url='login'))
class RecentArticlesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecentArticles.objects.all()
    serializer_class = RecentArticlesSerializer

# FooterBottomImg Views
@method_decorator(login_required(login_url='login'))
class FooterBottomImgListCreateAPIView(generics.ListCreateAPIView):
    queryset = FooterBottomImg.objects.all()
    serializer_class = FooterBottomImgSerializer

@method_decorator(login_required(login_url='login'))
class FooterBottomImgRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FooterBottomImg.objects.all()
    serializer_class = FooterBottomImgSerializer
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
