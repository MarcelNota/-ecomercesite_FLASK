# Importing

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomerce.db'

db = SQLAlchemy(app)

# Database Modelatiion

class Product(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(120) , nullable=False)
    price = db.Column(db.Float , nullable=False)
    description = db.Column(db.Text , nullable=True)
     

# Routes (Root route/ Initial page)
@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.json  # input sent by client
    if 'name' and 'price' in data:
        product = Product(name=data.get("name" , "Name not found"), price=data.get("price" , "Price not found"), description=data.get("description" , "Description not found"))    # to catch what the cllient typed (keys and values) ex: "name":"tv"
        db.session.add(product) # opens session and adds product
        db.session.commit()
        return "PRODUCT ADDED SUCCESSFULY"            # 2 ways of getting client data 1st name=data["name"]
    return jsonfy({"message":"INVALID PRODUCT DATA"}) # and name=data.get("name", "ERROR MESSAGE")
@app.route('/')
def welcome():
    return 'Bem Vindo'

if __name__ == "__main__":
    app.run(debug=True)