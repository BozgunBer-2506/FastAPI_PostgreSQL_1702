# FastAPI Order Management System

A professional REST API developed for managing users and orders, utilizing **FastAPI** and **PostgreSQL**. This project focuses on relational database management, data validation, and clean architectural patterns.

## 🚀 Key Features

- **Full CRUD Operations**: Create, Read, Update, and Delete users and orders.
- **Relational Mapping**: Orders are linked to users via Foreign Keys.
- **Data Integrity**: Powered by Pydantic v2 for robust input/output validation.
- **Automated Migrations**: Database schema tracking with Alembic.
- **Persistent Storage**: Data is safely stored in a local PostgreSQL instance.

## 🛠 Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Environment**: Python 3.10+
- **Server**: Uvicorn

## 📥 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/BozgunBer-2506/FastAPI_PostgreSQL_1702.git

cd FastAPI_PostgreSQL_1702
```

2. **Setup Virtual Environment**

```bash
python -m venv .venv

```

### Windows

```powershell
.venv\Scripts\activate

```

### Linux / WSL

```bash
source .venv/bin/activate
```
