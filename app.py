# Importing

from flask import Flask

app = Flask(__name__)

# Routes (Root route/ Initial page)

@app.route('/')
def welcome():
    return 'Bem Vindo'

if __name__ == "__main__":
    app.run(debug=True)