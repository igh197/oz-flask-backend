from flask import Flask
from requests import request
app= Flask(__name__)
import requests

@app.route('/')
def home():
    return 'Hello!'
@app.route('/about')
def about():
    return "About Page!" 
@app.route('/user/<username>')
def user_profile(username):
    return f'username: {username}'

@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url,data = data)


@app.route('/submit', methods=['GET','POST','PUT','DELETE'])
def submit():
    print(request.method)
    if requests.method=='GET':
        print('GET method')
    elif request.method=='POST':
        print('POST method',request.data)
    return 'success'


if __name__ == "__main__":

    app.run()
