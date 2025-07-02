import requests

def make_request(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def get_biggest_gainer(data):
    if not data:
        return None
    return data[0]

def format_stock_info(stock_info):
    if not stock_info:
        return "No stock data available."
    return (
        f"This is the biggest stock gainer: {stock_info['name']} Ticker: {stock_info['symbol']}\n"
        f"This is the price of the stock: {stock_info['price']}\n"
        f"This is the change percent of the stock: {stock_info['changesPercentage']}\n"
    )

def print_stock_info(stock):
    print(format_stock_info(stock))

if __name__ == "__main__":
    api_key = "5H9LohX4eRJoAHXeYftqgRrd2UrWkRdW"
    url = f"https://financialmodelingprep.com/stable/biggest-gainers?apikey={api_key}"
    data = make_request(url)
    stock = get_biggest_gainer(data)
    print_stock_info(stock)
