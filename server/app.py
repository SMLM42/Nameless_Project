#

from flask import Flask, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class Root(Resource):
    """"""

    ENPOINT = "/api"

    def get(self):
        """"""

        return {"status": "ok"}


for route in [Root]:
    api.add_resource(Root, Root.ENPOINT)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
    print("Server died")
