import requests

url="https://cdn-api.co-vin.in/api/v2/admin/location/districts/1"
response = requests.get(url, headers={
            "accept": "application/json",
            "Accept-Language": "hi_IN",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        })

print(response.json())