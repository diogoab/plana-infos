from flask import Flask, request, jsonify
from datetime import datetime
import pkg_resources

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

date =  datetime.now()
version = pkg_resources.get_distribution('flask').version
engine = Flask

@app.route("/", methods=['GET'])
def get_infos():
    return jsonify({"Timestamp": date,
    "Hostname": request.host,
    "Flask": version, 
    "Visitor ip": request.remote_addr}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')


