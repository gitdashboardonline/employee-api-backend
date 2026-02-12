# HRMS Lite – Employee & Attendance Management System

A lightweight Human Resource Management System built using:

- ⚡ FastAPI (Backend API)
- 🐘 PostgreSQL (Database)
- 🅰️ Angular (Frontend UI)
- ☁️ Render (Backend Deployment)
- 🌐 Netlify (Frontend Deployment)

---

## 🚀 Live Demo

Frontend: https://deluxe-manatee-696864.netlify.app/  
Backend API: https://employee-api-backend-54t8.onrender.com/docs

---

## 📦 Project Structure

```
hrms-project/
│
├── backend/          # FastAPI Backend
│   ├── app/
│   ├── requirements.txt
│   └── main.py
│
├── frontend/         # Angular Frontend
│   ├── src/
│   ├── angular.json
│   └── package.json
```

---

# 🖥️ Running Project Locally

---

# 🔹 1️⃣ Backend Setup (FastAPI + PostgreSQL)

## Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/hrms-backend.git
cd hrms-backend
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Setup PostgreSQL

Make sure PostgreSQL is installed and running.

Create database:

```sql
CREATE DATABASE hrms_db;
```

---

## Step 5: Configure Environment Variable

Create a `.env` file in backend root:

```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/hrms_db
```

If using Render DB externally:

```
DATABASE_URL=postgresql://user:password@host:5432/dbname?sslmode=require
```

---

## Step 6: Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

# 🔹 2️⃣ Frontend Setup (Angular)

## Step 1: Navigate to Frontend

```bash
cd hrms-frontend
```

---

## Step 2: Install Dependencies

```bash
npm install
```

---

## Step 3: Update API URL

Open:

```
src/environments/environment.ts
```

Set:

```typescript
export const environment = {
  production: false,
  apiUrl: 'http://localhost:8000'
};
```

---

## Step 4: Run Angular App

```bash
ng serve
```

Frontend runs at:

```
http://localhost:4200
```

---

# 🛠️ Features

- ✅ Employee CRUD
- ✅ Attendance Tracking
- ✅ Employee-wise Attendance View
- ✅ RESTful API
- ✅ PostgreSQL Integration
- ✅ Clean Architecture (Models + Services)
- ✅ Production Deployment Ready

---

# 🌐 Deployment

## Backend: Render

- Create PostgreSQL instance on Render
- Create Python Web Service
- Add environment variable:

```
DATABASE_URL=your_render_database_url
```

Start Command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

## Frontend: Netlify

Build Angular app:

```bash
ng build --configuration production
```

Publish Directory:

```
dist/hrms-frontend
```

Add `netlify.toml` file:

```
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

---

# 🔒 Environment Variables

Backend requires:

```
DATABASE_URL
```

Example:

```
postgresql://username:password@localhost:5432/hrms_db
```

---

# 📊 Tech Stack

| Layer     | Technology  |
|-----------|------------|
| Frontend  | Angular     |
| Backend   | FastAPI     |
| Database  | PostgreSQL  |
| ORM       | SQLAlchemy  |
| Deployment| Render + Netlify |

---

# 👩‍💻 Author

SHIVANGI RAUTELA  
GitHub: https://github.com/gitdashboardonline

---

# 📄 License

This project is developed for assessment purposes.
