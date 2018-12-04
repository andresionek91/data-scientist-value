from flask import Flask, render_template, request
import requests
import json

application = Flask(__name__)

@application.route('/')
@application.route('/index')
def home():
    #counting the quantity of objects on S3 bucket
    url = 'https://wucg3iz2r4.execute-api.us-east-2.amazonaws.com/default/count-kaggle-top20-objects'
    r = requests.get(url).json()

    return render_template('index.html', qty=r['size'])


@application.route('/score', methods=['POST', 'GET'])
def score():
    if request.method == 'POST':
        # get result from form and treat it
        input_json = request.form

        # create header and url
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = 'https://tk9k0fkvyj.execute-api.us-east-2.amazonaws.com/default/top20-predictor'

        # make POST request and load response
        r = requests.post(url, params=input_json, headers=header).json()['body']
        result = json.loads(r)

        # render the html template sending the variables
        return render_template("score.html", score=result['score'], proba=result['proba'])


if __name__ == '__main__':
    application.run(debug=True)





