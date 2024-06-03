from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    # path('activate/<uidb64>/<token>', views.activate, name="activate"),
    # path('image_generation', views.image_generation, name="image_generation"),
    path('coffee_shop', views.coffee, name="coffee"),
    path('list_coffee/<int:pk>', views.list_coffee, name="list_coffee"),
    path('delete_coffee/<int:pk>', views.delete_coffee, name="delete_coffee"),
    path('add_coffee', views.add_coffee, name="add_coffee"),
    path('update_coffee/<int:pk>', views.update_coffee, name='update_coffee'),
    path('order_coffee', views.order_coffee, name="order_coffee"),
    path('reset_cart/', views.reset_cart, name='reset_cart'),  # Thêm dòng này
    path("quantity_coffee/<int:pk>", views.quantity_coffee, name='quantity_coffee')

]