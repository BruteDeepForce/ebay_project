# ebay_integration/utils.py
import requests
from django.conf import settings

from ebay_project.cloudinary_config import upload_image

def add_product_to_ebay(product):
    url = "https://api.ebay.com/ws/api.dll"

    image_url = upload_image(product.image_url)  # Resmi yükle ve URL'yi al

    headers = {
        "X-EBAY-API-SITEID": "0",  # eBay site ID (Amerika için 0) buraya bakıcaz
        "X-EBAY-API-CALL-NAME": "AddItem",  # Ürün ekleme endpoint
        "X-EBAY-API-APP-ID": settings.EBAY_APP_ID,  # eBay Uygulama ID
        "X-EBAY-API-VERSION": "967",  # eBay API versiyonu
        "Content-Type": "text/xml"  # XML format
    }
    
    # eBay API'sine gönderilecek XML verisi
    xml_data = f"""
        <?xml version="1.0" encoding="utf-8"?>
        <AddItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
        <RequesterCredentials>
        <eBayAuthToken>{settings.EBAY_AUTH_TOKEN}</eBayAuthToken>
        </RequesterCredentials>
        <Item>
        <Title>{product.title}</Title>
        <Description>{product.description}</Description>
        <PrimaryCategory>
            <CategoryID>{product.category_id}</CategoryID>
        </PrimaryCategory>
        <StartPrice>{product.price}</StartPrice>
        <ConditionID>{product.condition}</ConditionID>
        <Currency>USD</Currency>
        <Country>US</Country>
        <PostalCode>95125</PostalCode>
        <ListingDuration>Days_7</ListingDuration>
        <ListingType>FixedPriceItem</ListingType>
        <DispatchTimeMax>3</DispatchTimeMax>
        <PaymentMethods>PayPal</PaymentMethods>
        <PayPalEmailAddress>{settings.EBAY_PAYPAL_EMAIL}</PayPalEmailAddress>
        <PictureDetails>
            <PictureURL>{image_url}</PictureURL>
        </PictureDetails>
        <Quantity>{product.stock_quantity}</Quantity>
        <ShippingDetails>
            <ShippingType>Flat</ShippingType>
            <ShippingServiceOptions>
                <ShippingServicePriority>1</ShippingServicePriority>
                <ShippingService>USPSMedia</ShippingService>
                <ShippingServiceCost>2.50</ShippingServiceCost>
            </ShippingServiceOptions>
        </ShippingDetails>
        <ReturnPolicy>
            <ReturnsAcceptedOption>ReturnsAccepted</ReturnsAcceptedOption>
            <RefundOption>MoneyBack</RefundOption>
            <ReturnsWithinOption>Days_30</ReturnsWithinOption>
            <ShippingCostPaidByOption>Buyer</ShippingCostPaidByOption>
        </ReturnPolicy>
        <Site>US</Site>
    </Item>
</AddItemRequest>
"""

    
    response = requests.post(url, headers=headers, data=xml_data)
    return response.text  # API'den dönen yanıtı alıyoruz
