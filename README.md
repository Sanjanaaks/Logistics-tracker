# 🚚 Smart Logistics Order Tracking System (SLOTS)

This is a full-stack backend project built using Flask, MongoDB, and JWT authentication. It provides APIs for user registration, login, and shipment tracking, along with a minimal HTML frontend to test the endpoints.

---

## 📦 Features
- ✅ User registration and login
- ✅ JWT-based authentication
- ✅ Shipment creation, tracking, and status updates
- ✅ Swagger documentation support
- ✅ Docker & Docker Compose setup
- ✅ Clean HTML+JS frontend interface


## 🧪 API Testing Instructions

### 🔧 Swagger UI (optional)
- Serve Swagger from `swagger.yaml`
- Use [https://editor.swagger.io](https://editor.swagger.io) and paste your YAML

### 🧪 Postman
You can test endpoints with:
- Method: POST or GET
- URL: `http://localhost:5000/api/...`
- Body: Raw JSON

Example:
```json
POST /api/register
{
  "email": "test@example.com",
  "password": "123456"
}
```

---

## 🛠 How to Run

### Option 1: Run with Python
```bash
pip install -r requirements.txt
python app/main.py
```
Navigate to [http://localhost:5000](http://localhost:5000)

### Option 2: Run with Docker Compose
```bash
docker-compose up --build
```
Then open: [http://localhost:5000](http://localhost:5000)

---

## 📂 Folder Structure
```
logistics-tracker/
├── app/
│   ├── templates/index.html
│   ├── static/style.css
│   ├── routes/user_routes.py
│   ├── routes/shipment_routes.py
│   ├── auth/jwt_handler.py
│   ├── main.py
│   ├── models.py
│   └── __init__.py
├── swagger.yaml
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```


## 📋 License
MIT License 
