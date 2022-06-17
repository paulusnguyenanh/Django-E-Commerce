from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/',views.contactus,name='contact'),
    path('promotion/',views.promotion,name='promotion'),
    path('about/', views.aboutus, name='about'),
    path('search/',views.search,name='search'),
    path('search_auto/',views.search_auto,name='search_auto'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_product'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('load/', views.load_more, name='load'),
    path('faq/', views.faq, name='faq'),
]