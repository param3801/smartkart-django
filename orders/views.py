from django.shortcuts import render,redirect
from carts.models import Cart,CartItem
from orders.form import OrderForm
from .models import Order,OrderProduct
import datetime


# Create your views here.
def placeorder(request):
  current_user = request.user
  cart_items = CartItem.objects.filter(user = current_user)
  cart_count = len(cart_items)
  if cart_count<=0:
    return redirect('store')
  
  grand_total = 0 
  tax = 0

  for cart_item in cart_items:
    total += (cart_item.product.price * cart_item.quantity)
    quantity += cart_item.quantity
  tax = (2*total)/100
  grand_total = tax+max

  

  if request.method == 'POST':
    form = OrderForm()
    if form.is_valid():
      data = Order()
      data.user = current_user
      data.first_name = form.cleaned_data['first_name']
      data.last_name = form.cleaned_data['lasr_name']
      data.phone = form.cleaned_data['phone']
      data.email = form.cleaned_data['email']
      data.address_line_1= form.cleaned_data['address_line_1']
      data.address_line_2 = form.cleaned_data['address_line_2']
      data.country = form.cleaned_data['country']
      data.city = form.cleaned_data['city']
      data.state = form.cleaned_data['state']
      data.order_note = form.cleaned_data['order_note']
      data.order_total = grand_total
      data.tax = tax
      data.ip = request.META.get('REMOTE_ADDR')
      data.save()

      yr = int(datetime.date.today().strftime('%Y'))
      dt = int(datetime.date.today().strftime('%d'))
      mt = int(datetime.date.today().strftime('%m'))
      d = datetime.date(yr,mt,dt)
      currnet_date = d.strftime('%Y%m%d')
      order_number = currnet_date + str(data.id )
      data.order_number = order_number
      data.save()
      return redirect('checkout')
  else:
      return redirect('checkout')




     




  


