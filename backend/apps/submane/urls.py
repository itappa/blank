from django.urls import path

from . import views
from . import views

app_name = "submane"

urlpatterns = [
    path("", views.subscription_list, name="index"),
]
