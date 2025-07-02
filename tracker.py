import os
import sqlite3
import google.generativeai as genai
from investment import Investment
from investment import extract_amount


try:
    my_api_key = "AIzaSyADnZyQXk2RN9KhJidpY13t2lXVDe33Rc8"
    genai.configure(api_key=my_api_key)
except KeyError:
    raise ValueError("API key not found. Please set the 'GENAI_KEY' environment variable.")


def ask_gemini(prompt):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You are a financial advisor. Give thoughtful and relevant financial decisions and recommendations."
    )
    response = model.generate_content(prompt)
    return response.text


def insert_into_table(category, amount, date):
    c.execute("""
        INSERT INTO expenses (category, amount, date)
        VALUES (?, ?, ?)
    """, (category, amount, date))
    conn.commit()
    print("Expense logged!")


def get_table():
    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    columnNames = [desc[0] for desc in c.description]
    result = " | ".join(columnNames) + "\n"
    for row in rows:
        result += " | ".join(str(item) for item in row) + "\n"
    return result


if __name__ == "__main__":
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS expenses")
    c.execute(
        "CREATE TABLE IF NOT EXISTS expenses (category TEXT, amount TEXT, date TEXT)"
    )
    conn.commit()

    investmentOptions = []
    while True:
        print("Welcome to FinSight! Please select an option from below!")
        print("-----------------------------------")
        print("Option 1: Log Expense\nOption 2: Get Gemini Reccomendation\nOption 3: Reccomended Stock\nOption 4: Show table\nOption 5: Exit")
        choice = input("Choice: ")

        if choice == "1":
            category = input("Please enter the category of your purchase: ")
            amount = input("Please enter the amount of your purchase: ")
            date = input("Please enter the date of your purchase (YYYY-MM-DD): ")
            insert_into_table(category, amount, date)
        elif choice == "2":
            income = input("Enter your income for this month: ")
            print("Gemini is thinking...")
            table = get_table()
            prompt = "Based off the following income " + income + "and the following table, provide me with some reccomendations with my budget as well as what you think about it, and where to mitigate spending and stuff. The remaining money I have left needs to be split between my savings account and my investing account. Assume I have a healthy savings account and explicitly tell me how much money I should transfer to my investment account. List this investment amount explicitly with 'AMOUNT:' in the response" + table
            response = ask_gemini(prompt)
            print(response)
            investment_api_key = "5H9LohX4eRJoAHXeYftqgRrd2UrWkRdW"
            url = f"https://financialmodelingprep.com/stable/biggest-gainers?apikey=5H9LohX4eRJoAHXeYftqgRrd2UrWkRdW"
            investment = Investment(investment_api_key)
            data = investment.make_request(url)
            investmentOptions = investment.get_biggest_gainers(data, extract_amount(response))
        elif choice == "3":
            if not investmentOptions:
                print("No budget plan has been created yet. Press 2 first")
                continue
            print("\nTop 5 Investment Options - Largest growth in 24 hours and within recommended budget")
            print(f"{'Company':<35.35} {'Ticker':<10.10} {'Price':>10} {'Change Percent':>15}")
            for stock in investmentOptions:
                investment.print_stock_info(stock)
            print("\n")
        elif choice == "4":
            print(get_table())
        elif choice == "5":
            break
        else:
            print("Please select a valid option!")

    conn.close()
