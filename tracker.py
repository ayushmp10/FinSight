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
c.execute(
    "CREATE TABLE IF NOT EXISTS expenses (category TEXT, amount REAL, date TEXT)"

)
conn.commit()


#def insert_into_table(category, amount, date):
 #   c.execute("INSERT INTO expenses (category, amount, date) VALUES ('{category}', {amount}, '{date})')")
  #  conn.commit()
   # print("Expenses logged!")

#insert_into_table("Grocery", 45.5, "2025-07-02")