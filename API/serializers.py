from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Goods.models import (
    Category, Product, Cart, Banner, SideMenu, ProductImg, CartProduct,
    Order, ProductEnter, FeatureProduct, RecentArticles, FooterBottomImg,
    CustomUser
)

from Goods.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'img']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'category', 'description']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'author', 'is_active', 'shopping_date']

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'title', 'sub_title', 'img', 'is_active']
        
class SideMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideMenu
        fields = ['id', 'name', 'price', 'img', 'quantity']

class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = ['id', 'product', 'img']

class CartProductSerializer(serializers.ModelSerializer):
    productImg = serializers.ImageField(source='productImg.img', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = CartProduct
        fields = ['id', 'productImg', 'product', 'product_name', 'cart', 'quantity', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'cart', 'fullname', 'email', 'phone', 'address', 'status']

class ProductEnterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product', 'quantity', 'old_quantity', 'date', 'description']


class FeatureProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureProduct
        fields = ['id', 'name', 'img', 'rating', 'price']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ['id', 'user', 'product']

class RecentArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentArticles
        fields = ['id', 'posted_by', 'comments', 'posted_at', 'type', 'img', 'title', 'body']

class FooterBottomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentArticles
        fields = ['call_center', 'location', 'title', 'facebook_link', 'twitter_link', 'linkedin_link']

class FooterBottomImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterBottomImg
        fields = ['id', 'img']
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
