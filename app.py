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
    if 'name' in data and 'price' in data:
        product = Product(name=data.get("name" , "Name not found"), price=data.get("price" , "Price not found"), description=data.get("description" , "Description not found"))    # to catch what the cllient typed (keys and values) ex: "name":"tv"
        db.session.add(product) # opens session and adds product
        db.session.commit()
        return jsonify({"message" : "PRODUCT ADDED SUCCESSFULY" }) 
    return jsonify({"message" : "INVALID PRODUCT DATA"}), 400  # 400 is code error for invalid inserted data                                                             
                                  
                                  
@app.route("/api/products/delete/<int:product_id>", methods=["DELETE"]) # dentro de <tipoDado e o nomeVariavel> , aspas podem ser duplos como simples
def delete_Product(product_id):
    # retrieve product from database
    # verify if it exists
    # if exists delete it from database
    # if dont exist return error 404 "PRODUCT NOT FOUND"
     
    product = Product.query.get(product_id)
    if product:                               # it could be (product != None:)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message" : "PRODUCT DELETED SUCCESSFULY" }) 
    return jsonify({"message" : "PRODUCT NOT FOUND IN DATABASE"}), 404  # 404 is code error for not found data
    
    
                                                                  
             # 2 ways of getting client data 1st name=data["name"]
             # and name=data.get("name", "ERROR MESSAGE")

@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,        # it could be "product_id" : product.id , but since we have specified the route it can be writen as "id": product.id
            "name": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "PRODUCT NOT FOUND"}), 404
    
    
@app.route('/')
def welcome():
    return 'Bem Vindo'

if __name__ == "__main__":
    app.run(debug=True)