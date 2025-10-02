from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/',views.dashboard_view, name = 'dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # new path for edit profile
    path('change_password/', views.change_password, name='change_password'),
    path('order_details/<int:order_id>/', views.order_details, name='order_details'),



]
