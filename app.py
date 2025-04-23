# Importing

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomerce.db'

db = SQLAlchemy(app)

# Database Modelatiion

class Product(db.Model):
    id = db.Colum(db.Integer , primary_key=True)
    name = db.Colum(db.String(120) , nullable=False)
    price = db.Colum(db.Float , nullable=False)
    description = db.Colum(db.Text , nullable=True)
     

# Routes (Root route/ Initial page)

@app.route('/')
def welcome():
    return 'Bem Vindo'

if __name__ == "__main__":
    app.run(debug=True)