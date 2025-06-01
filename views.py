from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from .models import Product


def home(request):
    return render(request, 'store/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            # Handle invalid login
            pass
    return render(request, 'store/cust_login.html')  # update if your template is named differently

def custom_logout(request):
    logout(request)
    return redirect('home')  # Or the name of your login URL pattern

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or home page after signup
        else:
            # Handle case where passwords don't match
            pass

    return render(request, 'store/Sign_up.html')


    # Optionally, you can override form validation if needed
    def form_valid(self, form):
        return super().form_valid(form)

@login_required
def dashboard(request):
    return render(request, 'store/dashboard.html')





from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetCompleteView

class CustomPasswordResetView(PasswordResetView):
    template_name = 'store/password_reset.html'  # This is the form page
    success_url = reverse_lazy('password_reset_done')  # Redirects after form submission
    email_template_name = 'store/password_reset_email.html'  # Email sent to user
    
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'store/password_reset_complete.html'
    success_url = reverse_lazy('login')



def products_view(request):
    products = Product.objects.all()
    cart = request.session.get('cart', [])
    return render(request, 'store/products.html', {'products': products, 'cart': cart})

def payment(request):
    cart = request.session.get('cart', [])
    subtotal = sum(item['price'] * item['quantity'] for item in cart)
    if request.method == 'POST':
        # Process payment (e.g., integrate Stripe/Razorpay)
        request.session['cart'] = []  # Clear cart after payment
        return redirect('password_reset_complete')  # Redirect to confirmation
    return render(request, 'store/payment.html', {'cart': cart, 'subtotal': subtotal})

from django.views.generic import TemplateView

class OrderConfirmationView(TemplateView):
    template_name = 'store/order_confirmation.html'

def cart(request):
    return render(request,'store/cart.html')

def about(request):
    return render(request,'external/about.html')

def contact(request):
    return render(request,'external/contact.html')