import requests

def get_btc_price(fiat_currency):
    # Convert the fiat currency to uppercase
    fiat_currency = fiat_currency.upper()

    # Check if the fiat currency is USD, EUR, or GBP
    if fiat_currency not in ["USD", "EUR", "GBP"]:
        print("Error: Accepted fiat currencies are USD, EUR, and GBP")
        return

    # Send a request to the CoinDesk API to get the current price of 1 BTC
    api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    params = {"currency": fiat_currency}
    response = requests.get(api_url, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception("Failed to get BTC price: status code {}".format(response.status_code))

    # Get the BTC price from the response
    data = response.json()
    btc_price = data["bpi"][fiat_currency]["rate_float"]

    return btc_price

# Test the function
while True:
    fiat_currency = input("Enter a fiat currency (e.g. USD, EUR, GBP): ")
    btc_price = get_btc_price(fiat_currency)
    if btc_price is not None:
        break

print("The current price of 1 BTC is {} {}".format(btc_price, fiat_currency))