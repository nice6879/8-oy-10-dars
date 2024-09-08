from django.db import models, transaction
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, AbstractUser, Group, Permission

class Banner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class SideMenu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    img = models.ImageField(upload_to="media/side_menu")


class Category(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField()
    img = models.ImageField(upload_to='category_img')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()

    def __str__(self):
        return self.name


class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='product-img')

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='carts')
    is_active = models.BooleanField(default=True)
    shopping_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.author.username if self.author else "Anonymous"


class CartProduct(models.Model):
    productImg = models.ForeignKey(ProductImg, on_delete=models.SET_NULL, null=True, related_name='cart_products')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.product

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, related_name='orders')
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    status = models.SmallIntegerField(
        choices=(
            (1, 'Tayyorlanmoqda'),
            (2, 'Yo`lda'),
            (3, 'Yetib borgan'),
            (4, 'Qabul qilingan'),
            (5, 'Qaytarilgan'),
        )
    )

    def __str__(self):
        return self.full_name


class ProductEnter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='entries')
    quantity = models.IntegerField()
    old_quantity = models.IntegerField(blank=True, null=True)  # Allow null for new instances
    date = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if not self:
                self.old_quantity = self.product.quantity
                self.product.quantity += int(self.quantity)
            else:
                try:
                    previous_entry = ProductEnter.objects.get(id=self.id)
                    quantity_diff = int(self.quantity) - previous_entry.quantity
                    self.product.quantity += quantity_diff
                    self.old_quantity = previous_entry.quantity
                except ObjectDoesNotExist:
                    # Handle case where the entry doesn't exist
                    pass
            self.product.save()
            super().save(*args, **kwargs)


class FeatureProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    img = models.ImageField(upload_to='media/feature_products')

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class RecentArticles(models.Model):
    posted_by = models.CharField(max_length=255)
    comments = models.IntegerField()
    posted_at = models.DateField()
    type = models.CharField(max_length=255)
    img = models.ImageField(upload_to='media/RecntArticles')
    title = models.CharField(max_length=255)
    body = models.TextField()




#info page:
class FooterBottom(models.Model):
    call_center = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    facebook_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    linkedin_link = models.URLField(max_length=255)

class FooterBottomImg(models.Model):
    img = models.ImageField(upload_to='media/footer_bottom')
    
    
    
    
    
    
class CustomUser(AbstractUser):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=20)
    email = models.EmailField()


    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add this line
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set_permissions',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
