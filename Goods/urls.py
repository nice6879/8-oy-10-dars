from django.urls import path, include
from Goods import views

urlpatterns = [
    path('', views.main, name='index'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
    path('user/', include('Goods.user.urls')),
    path('contact/', views.contact, name='contact'),
    
    #bannerni faqat creator userlar ishlatishi uchun html dan bu url_larga sorov yo'q
    #banner is only used by creator users, no request from html to these urls
    path('banners/', views.banner_list, name='banner_list'),
    path('banners/create/', views.banner_create, name='banner_create'),
    path('banners/<int:pk>/update/', views.banner_update, name='banner_update'),
    path('banners/<int:pk>/delete/', views.banner_delete, name='banner_delete'),

    path('footer', views.footer_bottom_list, name='footer_bottom_list'),
    path('detail/<int:pk>/', views.footer_bottom_detail, name='footer_bottom_detail'),
    path('create/', views.footer_bottom_create, name='footer_bottom_create'),
    path('update/<int:pk>/', views.footer_bottom_update, name='footer_bottom_update'),
    path('delete/<int:pk>/', views.footer_bottom_delete, name='footer_bottom_delete'),
    path('img/create/', views.footer_bottom_img_create, name='footer_bottom_img_create'),
]
