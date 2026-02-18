# FastAPI Order Management System

A professional REST API for managing users and orders, built with **FastAPI** and **PostgreSQL**.

## 🌐 Live Demo

**API Docs**: [https://fastapipostgresql1702-production.up.railway.app/docs](https://fastapipostgresql1702-production.up.railway.app/docs)

## 🚀 Features

- Full CRUD operations for users and orders
- Relational mapping via Foreign Keys
- Input/output validation with Pydantic v2
- Database migrations with Alembic
- Containerized with Docker for easy setup

## 🛠 Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Server**: Uvicorn
- **Container**: Docker
- **Cloud**: Railway

## 📦 Requirements

- Docker & Docker Desktop

## ⚡ Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/BozgunBer-2506/FastAPI_PostgreSQL_1702.git
cd FastAPI_PostgreSQL_1702
```

2. **Create your `.env` file**

```bash
cp .env.example .env
```

Edit `.env` with your own values:

```
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db:5432/kursapp
```

3. **Start the application**

```bash
docker-compose up --build
```

4. **Open the API docs**

```
http://localhost:8001/docs
```

## 🗂 Project Structure

```
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── routers/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

## 📝 Environment Variables

| Variable       | Description                  | Example                                      |
| -------------- | ---------------------------- | -------------------------------------------- |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://postgres:1234@db:5432/kursapp` |

## ☁️ Deployment

This project is deployed on **Railway** with automatic deployments on every push to `main`.

Environment variables are configured directly in the Railway dashboard — no `.env` file needed in production.

Crafted by The_Bozgun 2026
