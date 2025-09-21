from django.urls import path
from orders import views
urlpatterns = [
    path('placeorder/',views.placeorder,name="placeorder"),
    path('payment/',views.payment,name="payment"),
    path('order_complete/',views.order_complete,name="order_complete"),
    


]
