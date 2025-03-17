from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_random_cat():
    req = requests.get('https://api.thecatapi.com/v1/images/search')
    url = req.json()[0]['url']
    
    return url

@app.route("/", methods=["GET"])
def hello_world():
    cat_url = get_random_cat()
    return render_template('hello.html', cat_url=cat_url)

if __name__ == "__main__":
    app.run(debug=True, port=8000)