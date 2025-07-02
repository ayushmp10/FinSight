import unittest
from investment import Investment
import os
import tracker

class TestInvestment(unittest.TestCase):
    def setUp(self):
        self.api_key = "5H9LohX4eRJoAHXeYftqgRrd2UrWkRdW"
        self.url = f"https://financialmodelingprep.com/stable/biggest-gainers?apikey={self.api_key}"

    def test_get_biggest_gainer(self):
        data = [
            {"name": "Stock A", "symbol": "A", "price": 100, "changesPercentage": 20},
            {"name": "Stock B", "symbol": "B", "price": 200, "changesPercentage": 10},
        ]
        investment = Investment(self.api_key)
        data = investment.make_request(self.url)
        result = investment.get_biggest_gainer(data)
        self.assertEqual(result, data[0])

    def test_format_stock_info(self):
        stock = {"name": "Stock A", "symbol": "A", "price": 100, "changesPercentage": 10}
        result = Investment.format_stock_info(stock)
        self.assertEqual(result, "This is the biggest stock gainer: Stock A Ticker: A\nThis is the price of the stock: 100\nThis is the change percent of the stock: 10\n")
    
    
    def test_gemini(self):
        response = tracker.ask_gemini("Generate a one word answer")
        self.assertIsNotNone(response)
        self.assertEqual(response, "Invest\n")


if __name__ == "__main__":
    unittest.main()    



