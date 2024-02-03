
from django.conf import settings
from django.shortcuts import render


from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.order_by('name')
    return render(request, 'shop/index.html', {'products': products, 'media_url': settings.MEDIA_URL})
