from django.contrib import admin
from .models import Payment, Order, OrderProduct

admin.site.register(Payment)
# admin.site.register(Order)
admin.site.register(OrderProduct)

class OrderProductInline(admin.TabularInline):
  model = OrderProduct
  extra = 0
  readonly_fields = ('payment','user','product','quantity','product_price','ordered')
  

class OrderAdmin(admin.ModelAdmin):
  list_display = ('order_number','full_name','phone','email','city','order_total','status','is_ordered')
  list_filter = ('status','is_ordered')
  search_fields = ('order_number','first_name','last_name','phone','email')
  list_per_page = 20
  inlines = [OrderProductInline]
admin.site.register(Order,OrderAdmin)



# Register your models here.
