from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator


def index(request):
    products = Products.objects.all()

    #Search Code
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        products = products.filter(title__icontains=item_name)

    #Paginatition
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)  

    return render(request, 'shop/index.html', {'products':products})

def details(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'shop/details.html', {'product': product})

def checkout(request):
    if request.method=="POST":
        items = request.POST.get('all_items',"")
        name = request.POST.get('name', "")
        email =  request.POST.get('email',"")
        address = request.POST.get('address', "")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zip = request.POST.get('zip', "")
        total = request.POST.get('total_price',"")

        order = Order(name=name, email=email, address= address, city=city, state = state, zip=zip, total = total, items= items)
        order.save()
    
    return render(request, 'shop/checkout.html')