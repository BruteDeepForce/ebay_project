# ebay_integration/category_importer.py
import requests
import xml.etree.ElementTree as ET
from django.conf import settings
from .models import EbayCategory


def fetch_and_store_ebay_categories():
    url = "https://api.ebay.com/ws/api.dll"
    headers = {
        "X-EBAY-API-SITEID": "0",
        "X-EBAY-API-CALL-NAME": "GetCategories",
        "X-EBAY-API-APP-ID": settings.EBAY_APP_ID,
        "X-EBAY-API-VERSION": "967",
        "Content-Type": "text/xml",
    }
    
    xml_data = f"""
    <?xml version="1.0" encoding="utf-8"?>
    <GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
        <RequesterCredentials>
            <eBayAuthToken>{settings.EBAY_AUTH_TOKEN}</eBayAuthToken>
        </RequesterCredentials>
        <CategorySiteID>0</CategorySiteID>
        <DetailLevel>ReturnAll</DetailLevel>
        <ViewAllNodes>true</ViewAllNodes>
        <LevelLimit>2</LevelLimit>
    </GetCategoriesRequest>
    """

    response = requests.post(url, headers=headers, data=xml_data)

    if response.status_code != 200:
        raise Exception(f"eBay API error: {response.status_code} - {response.text}")

    # XML parse
    root = ET.fromstring(response.text)
    ns = {'ns': 'urn:ebay:apis:eBLBaseComponents'}

    for category in root.findall('.//ns:Category', ns):
        category_id = category.find('ns:CategoryID', ns).text
        category_name = category.find('ns:CategoryName', ns).text

        EbayCategory.objects.update_or_create(
            category_id=category_id,
            defaults={'category_name': category_name}
        )
