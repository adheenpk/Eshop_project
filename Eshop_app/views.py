from django.shortcuts import render
from Eshop_app.models import shop


# Create your views here.
def demo(request):
    product=shop.objects.all()
    return render(request,'index.html',{'products':product})



def detail(request,product_id):
    products=shop.objects.get(id=product_id)
    return render(request,'detail.html',{'product':products})









