import requests

class Investment:
    def __init__(self, api_key):
        self.api_key = api_key

    def make_request(self, url):
        try:
            response = requests.get(url)
            return response.json()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def get_biggest_gainer(self, data):
        if not data:
            return None
        return data[0] # return the first stock in the list which is the biggest gainer in this api structure

    def format_stock_info(stock_info):
        if not stock_info:
            return "No stock data available."
        return (
            f"This is the biggest stock gainer: {stock_info['name']} Ticker: {stock_info['symbol']}\n"
            f"This is the price of the stock: {stock_info['price']}\n"
            f"This is the change percent of the stock: {stock_info['changesPercentage']}\n"
        )

    def print_stock_info(self, stock):
        print(Investment.format_stock_info(stock))

if __name__ == "__main__":
    api_key = "5H9LohX4eRJoAHXeYftqgRrd2UrWkRdW"
    url = f"https://financialmodelingprep.com/stable/biggest-gainers?apikey=5H9LohX4eRJoAHXeYftqgRrd2UrWkRdW"
    investment = Investment(api_key)
    data = investment.make_request(url)
    stock = investment.get_biggest_gainer(data)
    investment.print_stock_info(stock)
