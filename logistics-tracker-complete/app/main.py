import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template
from pymongo import MongoClient
from app.routes.user_routes import user_bp
from app.routes.shipment_routes import shipment_bp

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/logistics_db'

mongo = MongoClient(app.config['MONGO_URI'])
db = mongo.get_database()

app.db = db
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(shipment_bp, url_prefix='/api')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
