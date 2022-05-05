from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from sklearn.linear_model import LinearRegression
from json import loads, dumps
import numpy as np

with open('model.json', 'r') as f:
    content = f.read()
    model = loads(content)

predictor = LinearRegression(n_jobs=-1)
predictor.coef_ = np.array(model)
predictor.intercept_ = np.array([0])

app = Flask(__name__)

@app.route('/')
def hello_world():
    params = request.args.get('input')
    parameters = params.split(",")
    X = [[int(i) for i in parameters]]
    outcome = predictor.predict(X=X)
    return str(outcome)


if __name__ == "__main__":
  app.run()