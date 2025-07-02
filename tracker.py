import os
from google import genai
from google.genai import types
import sqlite3

my_api_key = os.getenv('GENAI_KEY')
genai.api_key = my_api_key

client = genai.Client(
    api_key=my_api_key,
)

def ask_gemini(prompt):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
      system_instruction="You are acting as a financial advisor, give good financial decisions and reccomendations for a person"
    ),
    contents=prompt
    )
    return response.text


conn = sqlite3.connect('expenses.db')
c = conn.cursor()
c.execute(
    "CREATE TABLE IF NOT EXISTS expenses (category TEXT, amount REAL, date TEXT)"

)
conn.commit()
conn.close()

#def insert_into_table(category, amount, date):
