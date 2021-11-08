from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)
rashifal_list = ["mesh","brish","mithun","karkat","singha","kanya","tula","brischik","dhanu","makar","kumbha","meen"]
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def rashi():    
    if request.method == "POST" and request.form['rashi'].lower() in rashifal_list:
            rashi_name = request.form['rashi'].lower()
            r = requests.get(f"https://www.hamropatro.com/rashifal/daily/{rashi_name}")
            r_content = r.content
            soup = BeautifulSoup(r_content,"html.parser")
            rashi_content = soup.find_all("div",{"class":"desc"})
            rashifal= (rashi_content[0].find_all("p")[0].text.replace("\n",""))
            return render_template("index.html",rashifal=rashifal)
    return render_template("index.html",rashifal="Seems like you entered an invalid rashifal name ):")
            

if __name__ == "__main__":
    app.debug=True
    app.run()


