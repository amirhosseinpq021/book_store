# Generated by Django 5.0.6 on 2024-06-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(blank=True, max_length=20),
        ),
    ]
