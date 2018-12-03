from flask import Flask, render_template, request
import requests
from treat_data import treat_input
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/score', methods=['POST', 'GET'])
def score():
    if request.method == 'POST':
        result = request.form

        treated_input_json = treat_input(result)
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = 'https://tk9k0fkvyj.execute-api.us-east-2.amazonaws.com/default/top20-predictor'
        r = requests.post(url, params=treated_input_json, headers=header).json()['body']
        result = json.loads(r)

        return render_template("score.html", score=result['score'], proba=result['proba'])


if __name__ == '__main__':
    app.run(debug=True)





