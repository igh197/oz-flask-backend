from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api =Api(app)

items=[]

class Item(Resource):

    #조회
    def get(self):
        pass
    #생성
    def post(self):
        pass
    #수정
    def put(self):
        pass
    #삭제
    def delete(self):
        pass
