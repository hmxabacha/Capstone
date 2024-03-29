from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/',views.MenuItemView.as_view()),
    path('',views.restaurant),
    path('<int:pk>',views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
