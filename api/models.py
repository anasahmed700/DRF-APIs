import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    # Add any additional fields you want to include in your user model
    pass


class Product(models.Model):
    """
    Model representing a product.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def in_stock(self):
        """
        Check if the product is in stock.
        """
        return self.stock > 0

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Model representing an order.
    """
    class StatusChoices(models.TextChoices):
        PENDING = 'PE', 'Pending'
        CONFIRMED = 'CO', 'Confirmed'
        CANCELLED = 'CA', 'Cancelled'

    order_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="OrderItem", related_name='orders')
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    """
    Model representing an item in an order.
    """
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def item_subtotal(self):
        """
        Calculate the subtotal for this order item.
        """
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"
