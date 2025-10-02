from django.contrib import admin
from .models import Varition
from .models import ReviewRating,ProductGallery
import admin_thumbnails
from .models import Product

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]
   
admin.site.register(Product, ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', 'created_date')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')
admin.site.register(Varition, VariationAdmin)

#register reviewRating model
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'subject', 'rating', 'status', 'created_at')
    list_editable = ('status',)
    list_filter = ('status', 'created_at')
admin.site.register(ReviewRating, ReviewRatingAdmin) 

admin.site.register(ProductGallery)




