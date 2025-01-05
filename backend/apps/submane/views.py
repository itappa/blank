from django.shortcuts import render
from .models import Subscription

def subscription_list(request):
    subscriptions = Subscription.objects.all()
    total_cost = sum(sub.price for sub in subscriptions)
    category_costs = {}
    for sub in subscriptions:
        category_costs[sub.category] = category_costs.get(sub.category, 0) + sub.monthly_cost

    return render(request, 'apps/submane/list.html', {
        'subscriptions': subscriptions,
        'total_cost': total_cost,
        'category_costs': category_costs,
    })
