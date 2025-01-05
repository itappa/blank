from django.db import models
from django.contrib.auth import get_user_model
from math import ceil

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Payment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=20,
        choices=[
            ("CREDIT", "クレジット"),
            ("BANK", "銀行")
        ],
        default="CREDIT"
    )

    def __str__(self):
        return self.name

class Subscription(models.Model):
    name = models.CharField("サービス名", max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    billing_cycle = models.CharField(
        max_length=20,
        choices=[
            ('MONTHLY', '月'),
            ('YEARLY', '年'),
            ('QUARTERLY', '3ヶ月'),
            ('HALF-YEARLY', '6ヶ月'),
        ],
        default='MONTHLY'
    )
    next_billing_date = models.DateField()
    is_active = models.BooleanField(default=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def monthly_cost(self):
        if self.billing_cycle == 'YEARLY':
            return ceil(self.price / 12)
        elif self.billing_cycle == 'HALF-YEARLY':
            return ceil(self.price / 6)
        elif self.billing_cycle == 'QUARTERLY':
            return ceil(self.price / 3)
        return ceil(self.price)
    
    @property
    def yearly_cost(self):
        if self.billing_cycle == 'MONTHLY':
            return ceil(self.price * 12)
        elif self.billing_cycle == 'HALF-YEARLY':
            return ceil(self.price * 2)
        elif self.billing_cycle == 'QUARTERLY':
            return ceil(self.price * 4)
        return ceil(self.price)
    
    def __str__(self):
        return f"{self.name} - {self.monthly_cost}"
    
    @classmethod
    def get_category_summary(cls, user):
        categories = cls.objects.all()
        summary = []
        for category in categories:
            total = category.total_amount(user)
            if total > 0:
                summary.append({
                    'category': category.name,
                    'total': total,
                    'subscriptions': category.subscription_set.filter(
                        user=user,
                        is_active=True
                    )
                })
        return summary