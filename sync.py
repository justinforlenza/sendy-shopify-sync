import shopify
from pysendy import Sendy

API_KEY = '' # Shopify API KEY
PASSWORD = '' # Shopify API Password
STORE_URL = '' # Shopify Store SubDomain


SENDY_URL = '' # Sendy URL
SENDY_LIST = '' # Sendy Subscriber List

s = Sendy(base_url=SENDY_URL)
shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, STORE_URL)

shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()

customers = []
searching = True
page = 1

while searching:
    response = shopify.Customer.search(query='accepts_marketing:true', page=page)
    if len(response) > 0:
        customers += response
    else:
        searching = False
    page += 1

for customer in customers:
    try:
        name = customer.first_name + ' ' + customer.last_name
    except TypeError:
        pass
    try:
        s.subscribe(name=name, email=customer.email, list_id=SENDY_LIST, referrer='Shopify')
    except:
        pass
