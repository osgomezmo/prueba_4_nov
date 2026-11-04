from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({"mensaje": "API Python del parcial funcionando en puerto 5006 interno y 5007 externo"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)