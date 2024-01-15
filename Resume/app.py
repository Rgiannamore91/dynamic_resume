from flask import Flask, render_template
from helper import items

app = Flask(__name__, static_url_path="/static")

@app.route("/")

def index():
    return render_template('index.html', items=items)

@app.route("/form")
def form():
    return render_template('form.html')

if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)