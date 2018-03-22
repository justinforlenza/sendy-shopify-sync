# Sendy Shopify Sync 
Use this Python script to synchronize your Shopify Customers with your Sendy Mailing Lists

## Installation
Copy the `sync.py` script to wherever you want it to run. Reccomeneded on a server where you can create a cron-job for continous syncing. 

This script relies on the ShopifyAPI package and the pysendy package. Install them individually or use the included `requirements.txt` file.

Change the variables in the script file for your environment

```
API_KEY = '' # Your Shopify API KEY
PASSWORD = '' # Your Shopify API Password
STORE_URL = '' # Shopify Store SubDomain e.g. my-store


SENDY_URL = '' # Sendy URL e.g sendy.mydomain.com
SENDY_LIST = '' # Sendy Subscriber List(The subscriber list number on sendy)
```

