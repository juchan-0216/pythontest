import requests
import json
from bs4 import BeautifulSoup
import flask from Flask
app = Flask(__name__)

@app.route("/covid/")
def covkr():
    html = requests.get('https://coronaboard.kr')
    html = html.content.decode('utf8')
    jsonString = html.split('jsonData = ')[1]
    jsonString = jsonString.split(';')[0]
    dictionary = json.loads(jsonString)['chartForGlobal']['KR']

    result = {
        "confirmed": dictionary["confirmed_acc"][-1],
        "comfirmed_today": dictionary["confirmed"][-1],
        "death": dictionary["death_acc"][-1],
        "death_today": dictionary["death"][-1],
        "cured": dictionary["released_acc"][-1],
        "cured_today": dictionary["released"][-1]
    }
    return result

if __name__ == "__main__":
    app.run()
    
