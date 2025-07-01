import requests
api_key = "5H9LohX4eRJoAHXeYftqgRrd2UrWkRdW"
url = f"https://financialmodelingprep.com/stable/biggest-gainers?apikey={api_key}"

try:
    response = requests.get(url)
    data = response.json()
    bigStock = data[0]
    print(f"This is the biggest stock gainer: {bigStock['name']} Ticker: {bigStock['symbol']}")
    print(f"This is the price of the stock: {bigStock['price']}")
    print(f"This is the change percent of the stock: {bigStock['changesPercentage']}")
except Exception as e:
    print(f"Error fetching data: {e}")
