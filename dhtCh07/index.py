from flask import Flask, request, render_template, jsonify
from db_model import MySQL
import sensor_dht

app = Flask(__name__)
db = MySQL()

@app.route("/")
def home():
  return render_template("index.html")

@app.route('/api/now')
def insertdb():
    temp, hum = sensor_dht.get_now()
    result = db_model.add(temp, hum)
    return result

@app.route('/api/record')
def selectAll():
    result = db_model.selectAll()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")