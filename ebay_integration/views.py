# ebay_integration/views.py
from django.shortcuts import render
from .models import EbayProduct
from .utils import add_product_to_ebay as add_product_to_ebay_sdk
from .models import EbayCategory


from django.http import HttpResponse

def add_ebay_product(request):          #viewdan gelen valuelar
    if request.method == "POST":                
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        category_id = request.POST["category_id"]
        condition = request.POST["condition"]
        stock_quantity = request.POST["stock_quantity"]

        product = EbayProduct.objects.create(           #Django veritabanına kaydet
            title=title,
            description=description,
            price=price,
            category_id=category_id,
            condition=condition,
            stock_quantity=stock_quantity
        )

        # eBay API'ye ürün ekle
        ebay_response = add_product_to_ebay_sdk(product)
        return HttpResponse(f"eBay Yanıtı: {ebay_response}")
    
    categories = EbayCategory.objects.all()  # Tüm kategorileri al
    return render(request, "add_product.html", {"categories": categories})  # Kategorileri template'e gönder

