from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("add/", views.ItemAdd.as_view()),
    path("edit/<int:pk>/", views.ItemEdit.as_view()),
    path('<int:item_id>/', views.item_detail),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.CustomRegistrationView.as_view(), name='signup'),
    path('<str:username>/', views.UserProfileView.as_view(), name='user_profile'),
]