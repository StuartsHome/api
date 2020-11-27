from flask import Flask
from flask_restx import Resource, Api


# A minimal Flask-RESTX API looks like this:


app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}




if __name__ == '__main__':
    app.run(debug=True)