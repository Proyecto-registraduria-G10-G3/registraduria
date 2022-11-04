import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.candidate_blueprints import candidate_blueprints
from blueprints.political_party_blueprints import political_party_blueprints
from blueprints.table_blueprints import table_blueprints
from blueprints.vote_blueprints import vote_blueprints

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(candidate_blueprints)
app.register_blueprint(political_party_blueprints)
app.register_blueprint(table_blueprints)
app.register_blueprint(vote_blueprints)


@app.route("/", methods=["GET"])
def home():
    response = {"message": "welcome"}
    return jsonify(response)


# =======================Config and evecution code ====================
def load_file_config():
    with open("config.json", "r") as config:
        data = json.load(config)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("server running:http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
