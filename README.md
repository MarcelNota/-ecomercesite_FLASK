# 🛒 E-Commerce API — Flask

*A backend-oriented e-commerce API developed with Python and Flask, focused on RESTful endpoints, authentication, database persistence, and CRUD operations.*

This project was developed as part of my backend development learning journey, with the goal of understanding how to build a web API using **Flask**, interact with a relational database through **SQLAlchemy**, implement authentication, and expose API endpoints that can be tested with tools such as Postman.

---

## 📌 Overview

The project implements the backend of a simple e-commerce system.

The application provides functionality for:

- 👤 User authentication
- 🔐 Login and logout
- 🛒 Product management
- ➕ Product creation
- 📋 Product listing
- 🔍 Product lookup by ID
- 🔎 Product search
- ✏️ Product updates
- 🗑️ Product deletion
- 🔒 Protected routes using authentication
- 🗄️ Database persistence with SQLite
- 📄 API documentation using Swagger/OpenAPI

The application is built with **Flask** and uses **Flask-SQLAlchemy** for database interaction. Authentication and protected routes are handled with **Flask-Login**, while **Flask-CORS** provides Cross-Origin Resource Sharing support. :contentReference[oaicite:2]{index=2}

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Backend development |
| 🌶️ **Flask** | Web framework |
| 🗄️ **Flask-SQLAlchemy** | Database ORM |
| 🔐 **Flask-Login** | User authentication and session management |
| 🌐 **Flask-CORS** | Cross-Origin Resource Sharing |
| 🐘 **SQLite** | Relational database |
| 📄 **Swagger / OpenAPI** | API documentation |
| 📦 **pip** | Python dependency management |
| 🌿 **Git** | Version control |
| 🐙 **GitHub** | Repository hosting |

The project pins Flask 2.3.0, Flask-SQLAlchemy 3.1.1, Flask-Login 0.6.2, Flask-CORS 3.0.10, and Werkzeug 2.3.0 in `requirements.txt`. :contentReference[oaicite:3]{index=3}

---

## 🏗️ Architecture

*The application follows a simple Flask-based backend architecture in which HTTP requests are handled by Flask routes, business/data operations interact with SQLAlchemy models, and the database stores persistent data.*

```text
              🌐 Client
                 │
                 ▼
            🌶️ Flask App
                 │
        ┌────────┴────────┐
        ▼                 ▼
   🔐 Authentication   🛒 Product API
        │                 │
        └────────┬────────┘
                 ▼
          🗄️ SQLAlchemy
                 │
                 ▼
             🗄️ SQLite
```

---

## 📂 Project Structure

```text
-ecomercesite_FLASK/
│
├── 📁 SPECIAL_COMANDS/
│   └── Documentation screenshots and deployment/setup references
│
├── 📁 instance/
│   └── Application instance data
│
├── 📁 __pycache__/
│
├── 🐍 app.py
├── 📦 requirements.txt
├── 📄 swagger.yaml
└── 📄 README.md
```

---

# 🔐 Authentication

The application implements user authentication using **Flask-Login**.

The application initializes a `LoginManager` and configures a login route used when authentication is required. :contentReference[oaicite:4]{index=4}

### 🔑 Login

The API exposes:

```http
POST /login
```

The endpoint receives user credentials through the request body and authenticates the user.

A successful login creates an authenticated session, while invalid credentials return an unauthorized response. :contentReference[oaicite:5]{index=5}

### 🚪 Logout

```http
POST /logout
```

The logout endpoint is protected and requires authentication. :contentReference[oaicite:6]{index=6}

### 🛡️ Protected Routes

The project uses:

```python
@login_required
```

to protect operations that require an authenticated user.

For example, adding, updating, and deleting products require authentication. :contentReference[oaicite:7]{index=7}

---

# 🛒 Product Management

The application exposes REST-style endpoints for product management.

A product contains:

```text
🆔 id
🏷️ name
💰 price
📝 description
```

The corresponding database model is implemented using SQLAlchemy. :contentReference[oaicite:8]{index=8}

---

## 📋 Get All Products

```http
GET /api/products
```

*Returns the available products.*

The endpoint is documented in the project's Swagger specification. :contentReference[oaicite:9]{index=9}

---

## 🔍 Get Product by ID

```http
GET /api/products/{product_id}
```

*Retrieves the details of a specific product.*

Example:

```http
GET /api/products/1
```

If the product does not exist, the API returns:

```http
404 Not Found
```

The response contains:

```json
{
  "id": 1,
  "name": "Product name",
  "price": 100.0,
  "description": "Product description"
}
```

The implementation retrieves the product through SQLAlchemy and returns its main fields as JSON. :contentReference[oaicite:10]{index=10}

---

## 🔎 Search Products

```http
GET /api/products/search?q=<query>
```

*Searches for products using a query parameter.*

Example:

```http
GET /api/products/search?q=phone
```

The endpoint and query parameter are defined in the Swagger documentation. :contentReference[oaicite:11]{index=11}

---

## ➕ Add Product

```http
POST /api/products/add
```

*Creates a new product.*

Authentication is required.

Example request body:

```json
{
  "name": "Laptop",
  "price": 45000,
  "description": "Business laptop"
}
```

The application validates the presence of the `name` and `price` fields before creating the product record. :contentReference[oaicite:12]{index=12}

---

## ✏️ Update Product

```http
PUT /api/products/update/{product_id}
```

*Updates an existing product.*

Authentication is required.

Example:

```http
PUT /api/products/update/1
```

Request body:

```json
{
  "name": "Updated Laptop",
  "price": 48000,
  "description": "Updated description"
}
```

The implementation checks whether the product exists before applying the requested updates. :contentReference[oaicite:13]{index=13}

---

## 🗑️ Delete Product

```http
DELETE /api/products/delete/{product_id}
```

*Deletes an existing product.*

Authentication is required.

Example:

```http
DELETE /api/products/delete/1
```

If the product is not found, the API returns:

```http
404 Not Found
```

The delete operation removes the record through SQLAlchemy and commits the change to the database. :contentReference[oaicite:14]{index=14}

---

# 🔄 CRUD Workflow

The project demonstrates the standard CRUD lifecycle:

```text
➕ CREATE
   ↓
📖 READ
   ↓
✏️ UPDATE
   ↓
🗑️ DELETE
```

For products:

```text
POST   /api/products/add
GET    /api/products
GET    /api/products/{product_id}
PUT    /api/products/update/{product_id}
DELETE /api/products/delete/{product_id}
```

The available product operations are documented in `swagger.yaml`. :contentReference[oaicite:15]{index=15}

---

# 🗄️ Database

The project uses **SQLite** as its relational database.

The Flask application configures SQLAlchemy with:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomerce.db'
```

The database models are defined using Flask-SQLAlchemy. :contentReference[oaicite:16]{index=16}

---

## 🧱 Database Models

### 👤 User

The `User` model contains:

```text
🆔 id
👤 username
🔐 password
```

The username is configured as unique. :contentReference[oaicite:17]{index=17}

### 🛒 Product

The `Product` model contains:

```text
🆔 id
🏷️ name
💰 price
📝 description
```

:contentReference[oaicite:18]{index=18}

### 🛍️ CartItem

The `CartItem` model links users and products through foreign keys:

```text
User
 │
 └── CartItem
        │
        └── Product
```

The model stores:

```text
🆔 id
👤 user_id
📦 product_id
```

:contentReference[oaicite:19]{index=19}

---

# 🔗 API Flow

A typical authenticated product operation follows this flow:

```text
🌐 HTTP Request
       │
       ▼
🌶️ Flask Route
       │
       ▼
🔐 Authentication Check
       │
       ▼
🧩 Request Data
       │
       ▼
🗄️ SQLAlchemy
       │
       ▼
🐘 SQLite
       │
       ▼
📄 JSON Response
```

This project helped me understand how an HTTP request travels through a backend application and results in a database operation.

---

# 📄 API Documentation

The project includes a Swagger/OpenAPI specification:

```text
swagger.yaml
```

The documentation covers endpoints for:

- 🔐 Login
- 🚪 Logout
- 📋 Product listing
- 🔍 Product lookup
- 🔎 Product search
- ➕ Product creation
- ✏️ Product update
- 🗑️ Product deletion

The specification identifies the API as an **E-commerce API** and defines the available routes and expected responses. :contentReference[oaicite:20]{index=20}

---

# 🧪 API Testing

The API can be tested using tools such as:

- 🧪 Postman
- 📄 Swagger/OpenAPI tooling
- 💻 cURL

A typical workflow is:

```text
1️⃣ Start the Flask application
        ↓
2️⃣ Authenticate with /login
        ↓
3️⃣ Maintain the authenticated session
        ↓
4️⃣ Call protected product endpoints
        ↓
5️⃣ Inspect JSON responses
```

---

# ⚙️ Installation

## 📋 Prerequisites

Make sure you have:

- 🐍 Python 3 installed
- 📦 pip installed
- 🌿 Git installed

---

## 📥 Clone the Repository

```bash
git clone https://github.com/MarcelNota/-ecomercesite_FLASK.git
```

Move into the project directory:

```bash
cd -ecomercesite_FLASK
```

---

## 📦 Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The project dependencies are defined in `requirements.txt`. :contentReference[oaicite:21]{index=21}

---

# ▶️ Running the Application

Run the Flask application with:

```bash
python app.py
```

The API is configured to run locally and is documented in Swagger using:

```text
127.0.0.1:5000
```

:contentReference[oaicite:22]{index=22}

---

# 🧠 Learning Objectives

This project was developed to strengthen my understanding of backend development using Python and Flask.

### 🐍 Python Backend Development

- Build a backend application with Flask
- Define HTTP routes
- Handle HTTP requests
- Return JSON responses

### 🌐 RESTful API Development

- Work with HTTP methods
- Use route parameters
- Use query parameters
- Process JSON request bodies
- Return appropriate HTTP status codes

### 🗄️ Database Development

- Model relational data
- Use SQLAlchemy ORM
- Create relationships between models
- Persist application data in SQLite

### 🔐 Authentication

- Implement login/logout
- Manage user sessions
- Protect routes with authentication

### 🔄 CRUD

- Create records
- Read records
- Update records
- Delete records

### 📄 API Documentation

- Document endpoints using Swagger/OpenAPI
- Define request parameters
- Define response structures

---

# 📚 Concepts Practiced

```text
🐍 Python
🌶️ Flask
🗄️ Flask-SQLAlchemy
🔐 Flask-Login
🌐 Flask-CORS
🐘 SQLite
🔄 CRUD
🌐 REST API
📄 JSON
🔑 Authentication
🛡️ Protected Routes
🔗 SQLAlchemy Relationships
📋 HTTP Methods
📊 HTTP Status Codes
📄 Swagger / OpenAPI
🧪 API Testing
🌿 Git
🐙 GitHub
```

---

# 🚀 Learning Journey

*This project represents one of the backend development projects in my software engineering learning journey.*

```text
🐍 Python
      ↓
🌶️ Flask
      ↓
🌐 REST APIs
      ↓
🗄️ SQLAlchemy
      ↓
🔐 Authentication
      ↓
🔄 CRUD
      ↓
📄 Swagger / OpenAPI
      ↓
☕ Java
      ↓
🔗 JDBC ✅
      ↓
🌱 Spring Core
      ↓
🚀 Spring Boot
      ↓
🌐 REST APIs
      ↓
🗃️ Spring Data JPA
      ↓
🔐 Spring Security / JWT
      ↓
🐳 Docker
      ↓
🏗️ Microservices
```

---

# 👨‍💻 Author

## Marcel Paulo Nota

*Backend Software Engineering learner focused on Java, Spring Boot, REST APIs, SQL, databases, Docker, and microservices.*

### 🔗 Links

- 🐙 **GitHub:** https://github.com/MarcelNota
- 🌐 **Portfolio:** https://portfolio-marcelnota.onrender.com/
- 💼 **LinkedIn:** https://www.linkedin.com/in/marcelnota/
