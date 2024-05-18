from django.db import models
import datetime


class Item(models.Model):
    name = models.CharField(max_length=100)
    category_choices = (
        ("Техника", "Техника"),
        ("Одежда", "Одежда"),
        ("Сертификат", "Сертификат")
    )
    category = models.CharField(max_length=20, choices=category_choices)
    about = models.TextField(max_length=500)
    price = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo/', null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.TextField(max_length=100)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    review = models.TextField(max_length=1000)
    date = models.CharField(default = datetime.date.today().strftime('%d %B %Y'), editable = False)

    def __str__(self):
        return self.review