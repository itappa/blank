from django.contrib import admin
from .models import Category, Payment, Subscription

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "display_price", "billing_cycle", "monthly_cost", "yearly_cost", "payment")

    def display_price(self, obj):
        return int(obj.price)