# Importing

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager , login_required , logout_user , current_user       #para autenticacao de usuarios, login required para protecao de rotas(exigencia de autenticacao para uso das mesmas)

app = Flask(__name__)
app.config['SECRET_KEY'] = "TAYLAN#333"                              # chave secreta para o Login_manager gerenciar e obrigatorio, NO POSTMAN IR AO HEADERS E VER SESSAO DE COOKIES (NO CAMPO DE TESTE DA ROTA LOGIN)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomerce.db'


login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)                         # para receber a aplicacao
login_manager.login_view = 'login'                          # usar nome da rota do login que e '/login' mas sem por a barra e aspas (login)
CORS(app)

# Database Modelatiion
# User (id, username, password)
# open terminal (flask shell), (db.drop_all()-> limpa todo banco de dados para sua recriacao), (db.create_all() ->pega toda modelagem e transforma em tabelas ), (db.session.commit()-> armazena conexao com banco ), (db.session.commit()-> session armazena conexao com banco, commit torna efectiva as mudancas ) ) , exit()

class User (db.Model, UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique = True)
    password = db.Column(db.String(80), nullable=False)
    cart = db.relationship('CartItem', backref='user', lazy= True)     # db.relation to vinculate user and cart (CartItem) is the relation between the tables, lazy is to limitate the fetch of data on (user) 
                                                                       # note: it is at logical level it will not be reflected as a table
                                                                       # we created at User model because it is the user who adds the products


# Database Modelatiion  
# Product (id, name, price, description)
# open terminal (flask shell), (db.create_all()->pega toda modelagem e transforma em tabelas ), (db.session.commit()-> armazena conexao com banco ), (db.session.commit()-> session armazena conexao com banco, commit torna efectiva as mudancas ), exit()

class Product(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(120) , nullable=False)
    price = db.Column(db.Float , nullable=False)
    description = db.Column(db.Text , nullable=True)
     
  
  
class CartItem(db.Model):
    id = db.Column(db.Integer , primary_key=True)                                       # id of the chart
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)           # picking up the id from user table (here it becomes foreign key)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)     # picking up the id from product table (here it becomes foreign key)
    
       
     
# Autenticacao
# Funcao para controlar rotas protegidas, sempre que houver requisicoes em rotas protegidas, deve por no inicio de todas rotas protegidas

@login_manager.user_loader                   # Funcao para controlar rotas protegidas, sempre que houver requisicoes em rotas protegidas, deve por no inicio de todas rotas protegidas
def load_user(user_id):
    return User.query.get(int(user_id))      # get(int(user_id)) normally the get() belongs to String class, it comes as a String, so we converted it to int because (user_id) is int


@app.route('/login', methods=["POST"])
def login():
    data = request.json                # input sent by client
   # data.get("username")     podia ser data["username"], mas nao e viavel pois a excecao aparece no body, pode falhar encontrar o dado
    user = User.query.filter_by(username = data.get("username")).first()      # em norma o filtro e feito por id, aqui podemos fazer filtro por outra coisa , beste caso por username, sem o FIRST ele daria a lista de usuarios, mas como existe o FIRST ele dars apenas o 1o user
    
    if user and data.get("password") == user.password:
                login_user(user)                                              # metodo importado acima
                return jsonify({"message" : "PRODUCT ADDED SUCCESSFULY" })
    return jsonify({"message" : "UNAUTHORIZED USER, INVALID CREDENTIALS" }) , 401


@app.route('/logout', methods=["POST"])
@login_required                                    # obriga autenticacao para uso desta rota
def logout():
    logout_user()                                  # nao precisa de passar user por parametro
    return jsonify({"message" : "LOGOUT SUCCESSFULY" })


@app.route('/api/products/add', methods=["POST"])  # para adicionar produtos
@login_required                                    # obriga autenticacao para uso desta rota
def add_product():
    data = request.json  # input sent by client
    if 'name' in data and 'price' in data:
        product = Product(name=data.get("name" , "Name not found"), price=data.get("price" , "Price not found"), description=data.get("description" , "Description not found"))    # to catch what the cllient typed (keys and values) ex: "name":"tv"
        db.session.add(product) # opens session and adds product
        db.session.commit()     # puts the record on the database  
        return jsonify({"message" : "PRODUCT ADDED SUCCESSFULY" }) 
    return jsonify({"message" : "INVALID PRODUCT DATA"}), 400  # 400 is code error for invalid inserted data                                                             
                                  
                                  
@app.route("/api/products/delete/<int:product_id>", methods=["DELETE"]) # dentro de <tipoDado e o nomeVariavel> , aspas podem ser duplos como simples
@login_required                                    # obriga autenticacao para uso desta rota
def delete_Product(product_id):
    # retrieve product from database
    # verify if it exists
    # if exists delete it from database
    # if dont exist return error 404 "PRODUCT NOT FOUND"
     
    product = Product.query.get(product_id)
    if product:                               # it could be (product != None:)
        db.session.delete(product)            # opens session and deletes product
        db.session.commit()                   # puts the record on the database
        return jsonify({"message" : "PRODUCT DELETED SUCCESSFULY" }) 
    return jsonify({"message" : "PRODUCT NOT FOUND IN DATABASE"}), 404            # 404 is code error for not found data
    
    
                                                                  
             # 2 ways of getting client data 1st name=data["name"]
             # and name=data.get("name", "ERROR MESSAGE")

@app.route("/api/products/<int:product_id>", methods=["GET"])   # para pegar produtos por id
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

@app.route("/api/products/update/<int:product_id>", methods=["PUT"])  # para actualizar os produtos
@login_required                                    # obriga autenticacao para uso desta rota
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "PRODUCT NOT FOUND"}), 404
    
    data = request.json
    if "name" in data:
        product.name = data['name']
        
    if "price" in data:
        product.price = data['price']
        
    if "description" in data:
        product.description = data['description']        
    
    db.session.commit()           # to store the record at the database      
                                  # at POST and DELETE we use "db.session.add/delete" to retrieve or delete at the database
    return jsonify({"message": "PRODUCT SUCCESFULLY UPDATED"}), 200 #putting the "200" at the end is optional

@app.route("/api/products", methods = ["GET"])       # para listar todos produtos
def get_products():
    products = Product.query.all()                  # products(in plural) because its a list
    product_list = []
    for product in products:
        product_data = {
            "id": product.id,                       # it could be "product_id" : product.id , but since we have specified the route it can be writen as "id": product.id
            "name": product.name,
            "price": product.price,
        }
        product_list.append(product_data)
    
    return jsonify(product_list)
    
# Routes for cart

@app.route("/api/cart/add/<int:product_id>", methods=["POST"])
@login_required 
def add_to_cart(product_id):                 # need to have user and product
    user = User.query.get(int(current_user.id))   # to get the current user logged    
    
    product = Product.query.get(product_id)
    
    if user and product:                         # same as IF USER AND PRODUCT EXIST
        cart_item = CartItem(user_id=user.id , product_id=product.id)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({'message': 'ITEM ADDED TO THE CHART SUCESSFULLY'}), 200 # THE 200 CODE IS OPTIONAL
        return jsonify({'message': 'FAILED TO ADD ITEM TO THE CHART '}), 400 # THE 200 CODE IS OPTIONAL
    return 



if __name__ == "__main__":
    app.run(debug=True)