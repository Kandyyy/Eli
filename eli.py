import typer
import requests, json
from dotenv import load_dotenv
import os
from tabulate import tabulate
import webbrowser
from googlesearch import search

app = typer.Typer()
load_dotenv('.env')
url = os.getenv('API_KEY')

class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found")
      for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=10,pause=2):
         count += 1
         #print (count)
         print(i + '\n')

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

@app.command()
def open(app_name: str):
    if app_name == "discord":
        os.startfile(r"C:\Users\hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk")
    elif app_name == "brave":
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk") 
    elif app_name == "whatsapp":
        webbrowser.open("https://web.whatsapp.com/")
    elif app_name == "spotify":
        os.startfile(r"C:\Users\hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk")

@app.command()
def search(query: str):
    gs = Gsearch_python(query)
    gs.Gsearch()


if __name__ == "__main__":
    app()