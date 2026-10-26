#importing libraries
import json
import sys
import requests


try:
    num_bc = float(sys.argv[1])
    info = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=384ce8294773be70b5873708805e37db1fe342dcd22fd3da6bf4bd75c6f8d4ee")
    f = info.json()
    price = float(f["data"]["priceUsd"])

except requests.RequestException:
    sys.exit(1)
except ValueError:
    sys.exit(1)


cost = num_bc*price
cost = round(cost , 4)
print(f"${cost:,}" , end = " ")
