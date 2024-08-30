from django.urls import path
from . import views

app_name = 'parts_of_computer_app'

urlpatterns = [
    path("", views.home_view, name="home"),

    path('signup/', views.signup, name="signup"), # tamamlanmadı

    path('ara/', views.product_by_search, name='product_by_search'),
    
    path("<int:categoryID>", views.getProductsByCategoryID),
    path("<str:category>", views.getProductsByCategory, name="ProductsByCategory"),


    path("urun-detaylari/<int:id>/", views.detay_view, name="urun-detaylari"),
  
    path("sort/", views.products_by_cost, name="products_by_cost"),     

    path('about-us/', views.about_us, name="about_us"),
    path("contact/", views.contact, name="contact" ),



    path('sepet/', views.sepet_detay, name='sepet_detay'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('increment_cart_item/<int:item_id>/', views.increment_cart_item, name='increment_cart_item'),
    path('decrease_cart_item/<int:item_id>/', views.decrease_cart_item, name='decrease_cart_item'),




]