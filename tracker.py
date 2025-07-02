import os
import sqlite3
import google.generativeai as genai


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


conn = sqlite3.connect('expenses.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS expenses")
c.execute(
    "CREATE TABLE IF NOT EXISTS expenses (category TEXT, amount TEXT, date TEXT)"

)
conn.commit()


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
        print("Gemini is thinking...")
        table = get_table()
        prompt = "Based off the following table, provide me with some reccomendations with my budget as well as what you think about it, and where to mitigate spending and stuff. Also, tell me how much money I should invest into stocks. Clearly say AMOUNT: and then the amount to invest. I want a clear dollar amount after the AMOUNT: every single time, no matter how little the table is or how little context you have" + table
        print(ask_gemini(prompt))
    elif choice == "3":
        break
    elif choice == "4":
        print(get_table())
    elif choice == "5":
        break
    else:
        print("Please select a valid option!")

conn.close()