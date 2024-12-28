from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Authors(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='cover/', blank=True)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField(blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])

    def get_discounted_price(self):
        """
        این متد قیمت کتاب با در نظر گرفتن تخفیف را محاسبه می‌کند.
        """
        if self.discount_percentage > 0:
            discount_amount = (self.discount_percentage / 100) * self.price
            return self.price - discount_amount
        return self.price  # اگر تخفیفی نباشد، قیمت اصلی کتاب بازگشت داده می‌شود.


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    # def get_absolute_url(self):
    #     return reverse('book_detail', args=[self.pk])

