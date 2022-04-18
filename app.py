from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"path":"ping","code":"200", "result":"ok"})


@app.route("/health")
def health():
    return jsonify({"health":"health","code": "200", "result": "ok"})

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"code":"404", "result":"page not found"}), 404

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"code":"404", "result":"page not found"}), 404

@app.errorhandler(500)
def error_server(e):
    return jsonify({"code":"500", "result":"server error"}), 500



if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")