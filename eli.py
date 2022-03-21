import typer
import requests, json
from dotenv import load_dotenv
import os
from tabulate import tabulate

app = typer.Typer()
load_dotenv('.env')
url = os.getenv('API_KEY')

@app.command()
def hi():
    print(f"Hello Kandy!")

@app.command()
def weather():
    response = requests.get(url)
    json_response = response.json()
    x = json_response["main"]
    temp, humidity, degree_sign = x["temp"], x["humidity"], u'\N{DEGREE SIGN}'
    z= json_response["weather"]
    weather_description = z[0]["description"]
    result="It is " + str("{:.2f}".format(temp-273.15)) + degree_sign + "C" + "," + weather_description + "\nWith a humidity of " + str(humidity) + "%"
    table = [[result]]
    print(tabulate(table, tablefmt='grid'))

if __name__ == "__main__":
    app()