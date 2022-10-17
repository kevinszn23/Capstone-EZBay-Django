from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):

    name = models.CharField(max_length=100, default="Nike Stussy Spiridon Fossil")
    img = models.CharField(max_length=500, default="https://i.ebayimg.com/images/g/vToAAOSwNPti-wZp/s-l500.jpg")
    ships_from = models.CharField(max_length=100, default="Ships from United States")
    price = models.CharField(max_length=100, default="US $300.00")
    condition = models.CharField(max_length=100, default="Pre-owned")
    shipping_details = models.CharField(max_length=200, default="US $13.00, Secure delivery with tracking, Located in: Jersey City, New Jersey, United States")
    delivery = models.CharField(max_length=100, default="Estimated between Thu, Oct 20 and Tue, Oct 25 to 02171")
    returns = models.CharField(max_length=200, default="This item is final sale and cannot be returned")
    payments = models.CharField(max_length=100, default="PayPal, Google Pay, Visa, Mastercard, American Express, Discover")
    authenticity = models.TextField(max_length=500, default="This item is verified by professionally trained authenticators before delivery")
    money_back = models.TextField(max_length=500, default="Get the item you ordered or get your money back.")
    seller_information = models.TextField(max_length=500, default="codingconnoseiur23 (999 ✭), 99.3% Positive feedback")
    bio = models.TextField(max_length=500, default="This item is super useful")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']