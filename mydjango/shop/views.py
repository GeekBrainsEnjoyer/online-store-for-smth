from django.views import generic


from .models import Product

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'products_list'

    def get_queryset(self):
        return Product.objects.order_by('name')
