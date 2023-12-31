from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("details/<str:item_title>", views.detail, name="detail"),
    path("watch_list", views.watch_list, name="watch_list"),
    path("cateories", views.categories, name="categories"),
    path("categories/<str:category>", views.category, name="category")
]
