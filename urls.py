from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import login_view
from .views import CustomPasswordResetView
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Custom password reset view (optional: your own subclass view)
  path('forgot_password/', CustomPasswordResetView.as_view(), name='forgot_password'),

    path('password_reset_done/', 
         TemplateView.as_view(template_name='store/password_reset_done.html'), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='store/password_reset_confirm.html'), 
         name='password_reset_confirm'),

  # This view handles the password change form (POST happens here)
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name='store/password_reset_confirm.html',
    success_url=reverse_lazy('password_reset_complete')
), name='password_reset_confirm'),

# This view only renders the success page after password is changed
path('password_reset_complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # Optional alias for login route (make sure it's not conflicting)
    path('accounts/login/', login_view, name='login'),

    path('products', views.products_view, name='products'),
    path('payment/', views.payment, name='payment'),
    path('cart', views.cart, name='cart'),

    path('order-confirmation/', views.OrderConfirmationView.as_view(), name='order_confirmation'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact')

    

]
