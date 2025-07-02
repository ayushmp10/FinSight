import requests
import re


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

    def get_biggest_gainers(self, data, amount):
        if not data:
            print("no data")
            return None
        stocks = []
        for stock in data:
            try:
                price = float(stock['price'])
            except (KeyError, ValueError, TypeError):
                print("error")
                continue  # skip stocks with invalid price
            if price <= amount:
                stocks.append(stock)
                if len(stocks) == 5:
                    break
        return stocks

    def format_stock_info(stock_info):
        if not stock_info:
            return "No stock data available."
        return (
            f"{stock_info['name']:<35.35} "
            f"{stock_info['symbol']:<10.10} "
            f"{float(stock_info['price']):>10.2f} "
            f"{float(stock_info['changesPercentage']):>15.2f}"
        )

    def print_stock_info(self, stock):
        print(Investment.format_stock_info(stock))


def extract_amount(input_string):
    match = re.search(
        r'amount[:\s\*]*\$?\s*([0-9,]+(?:\.[0-9]+)?)',
        input_string,
        re.IGNORECASE
    )
    if match:
        # Remove commas for thousands, e.g., 2,000 -> 2000
        amount_str = match.group(1).replace(',', '')
        return float(amount_str)
    return None


if __name__ == "__main__":
    api_key = "5H9LohX4eRJoAHXeYftqgRrd2UrWkRdW"
    url = f"https://financialmodelingprep.com/stable/biggest-gainers?apikey={api_key}"
    investment = Investment(api_key)
    data = investment.make_request(url)
    stocks = investment.get_biggest_gainers(data, 50)
    print(f"{'Company':<35} {'Ticker':<10} {'Price':<10} {'Change Percent':<15}")
    for stock in stocks:
        investment.print_stock_info(stock)
