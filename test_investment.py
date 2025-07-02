import unittest
from investment import Investment
import os
import tracker

class TestInvestment(unittest.TestCase):
    def setUp(self):
        self.api_key = "5H9LohX4eRJoAHXeYftqgRrd2UrWkRdW"
        self.url = f"https://financialmodelingprep.com/stable/biggest-gainers?apikey={self.api_key}"

    def test_get_biggest_gainers(self):
        data = [
            {"name": "Stock A", "symbol": "A", "price": 100, "changesPercentage": 100},
            {"name": "Stock B", "symbol": "B", "price": 200, "changesPercentage": 102},
            {"name": "Stock C", "symbol": "C", "price": 200, "changesPercentage": 101},
            {"name": "Stock D", "symbol": "D", "price": 200, "changesPercentage": 110},
            {"name": "Stock E", "symbol": "E", "price": 200, "changesPercentage": 120},
            {"name": "Stock F", "symbol": "F", "price": 200, "changesPercentage": 10},
            {"name": "Stock G", "symbol": "G", "price": 250, "changesPercentage": 200}
        ]
        investment = Investment(self.api_key)
        data = investment.make_request(self.url)
        result = investment.get_biggest_gainers(data, 200)
        self.assertEqual(result, data[:5])

    def test_format_stock_info(self):
        stock = {"name": "Stock A", "symbol": "A", "price": 100, "changesPercentage": 10}
        result = Investment.format_stock_info(stock)
        expected = (
            f"{'Stock A':<35.35} "
            f"{'A':<10.10} "
            f"{100:>10.2f} "
            f"{10:>15.2f}"
        )
        self.assertEqual(result, expected)
    
    
    def test_gemini(self):
        response = tracker.ask_gemini("Generate a one word answer")
        self.assertIsNotNone(response)
        self.assertEqual(response, "Invest\n")


if __name__ == "__main__":
    unittest.main()
