from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Book():
    id: int
    name: str
class HelloWorld(Resource):
    def get(self, id, kkkkkk):

        return {'hello': 'world'}

def calib():
    pass

def norm():
    pass

class HelloMir(Resource):
    def get(self):
        return {'111': '111'}
    def post(self, file):
        normalzied = norm(file)

        return
api.add_resource(HelloMir, '/kek/a*')
api.add_resource(HelloWorld, '/kek/ab')

if __name__ == '__main__':
    app.run(debug=True)