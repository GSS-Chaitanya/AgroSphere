from django.db import models
from django.contrib.auth.models import User

# 🌾 Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# 🧺 Product Model
class Product(models.Model):
  class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    rating = models.FloatField(default=0)
    reviews_count = models.IntegerField(default=0)
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# 🛒 Cart Item Model
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.product.price * self.quantity

# 📦 Order Model
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(CartItem)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    shipping_address = models.TextField()

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    def total_cost(self):
        return sum(item.total_price() for item in self.cart_items.all())
