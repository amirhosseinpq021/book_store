from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    discount_percentage_category = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Percentage discount for this category (0-100)."
    )

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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    book_discount_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Percentage discount for this book (0-100)."
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])

    def get_discounted_price(self):
        """
        Calculate the final discounted price based on book and category discounts.
        The highest discount (book or category) will be applied.
        """
        category_discount = (
            self.category.discount_percentage_category
            if self.category and self.category.discount_percentage_category > 0
            else 0
        )
        max_discount = max(self.book_discount_percentage, category_discount)
        discount = (self.price * max_discount) / 100
        return self.price - discount

    def save(self, *args, **kwargs):
        # Apply discount before saving
        if self.category and self.category.discount_percentage_category > 0:
            discount = (self.price * self.category.discount_percentage_category) / 100
            self.price -= discount
        super().save(*args, **kwargs)


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

