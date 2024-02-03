from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%b/%d/')
    description = models.TextField()
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return f'{self.name} {self.price}'
