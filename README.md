# OlleFlow

As a backend web developer I never created a true portfolio project. The time has come to change that. 🫶

For this project I use the following sources:

- https://fastapi.tiangolo.com
- https://docs.pydantic.dev/latest/
- https://sqlmodel.tiangolo.com
- Forums: stackoverflow, reddit
- AI: ChatGPT, GitHub Copilot

Yes. I use AI. 🤖 It speeds up the development process.
Do I only rely on AI? Not at all. 🤡 Vibe coding is for the weak. I use the brain 🧠

---

## 📌 Overview

> A personal productivity backend for managing tasks, focus sessions, and deep work habits — built with FastAPI, PostgreSQL, and Redis.

**OlleFlow** is a scalable, async-first backend project built to support digital workers in managing their tasks, tracking focus sessions, and analyzing productivity patterns. Think of it as the API backbone of a personal productivity system — part Pomodoro tracker, part task manager, part focus-intelligence engine.

This project is ideal for backend prototyping, architecture demonstration, and feature-driven learning. It's designed with testability, modularity, and long-term expansion in mind.

---

## 🧠 Core Tech Stack

- **FastAPI** – Modern, async-first web framework
- **SQLModel** – Pydantic + SQLAlchemy for models, validations, and ORM
- **PostgreSQL** – Primary database
- **Redis** – Used for caching, rate limiting, and optionally pub/sub or background jobs
- **Alembic** – Database migrations
- **Pytest** – Unit and integration testing
- **Docker** – Environment containerization
- **Environment-based config** – `.env` driven settings

---

## 📂 Structure

```bash
.
├── models/        # SQLModel ORM models
├── schemas/       # Pydantic request/response schemas
├── services/      # Business logic services
├── crud/          # Generic and custom CRUD layers
├── api/           # Routers and endpoint logic
├── db/            # DB session and migration utils
├── alembic/       # Database migration setup
├── .env           # Environment configuration
├── tests/         # Pytest-based test coverage
└── main.py        # App entrypoint
```

## 🔧 Features (So Far)

- ✅ Clean, async CRUD operations
- ✅ User creation endpoint
- ✅ Base abstractions for services, schemas, and endpoints
- ✅ Alembic migrations + reset support
- ✅ Project structured for scalability and maintainability

## 🧱 Coming Soon

- Unit tests for services (time logic, task/session flow)
- Integration tests for route behavior and status codes
- Mocked Redis and database tests
- Parametrized edge cases (e.g., overlapping sessions, missing data)
- Focus sessions tracking logic
- Tagging system
- Project grouping
- Weekly productivity stats endpoint
- Caching and rate limiting
- JWT + refresh token auth

## 🚀 Getting Started

```bash

# Clone the repo
git clone https://github.com/yourname/olleflow.git
cd olleflow

# Install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

#Create a .env file at the root with the following content:
DATABASE_URL=postgresql+asyncpg://olleflow-admin:olleflow-admin-123@localhost:5432/olleflow

# Set up the DB
docker compose -f docker-compose.postgres.yml up -d

alembic upgrade head

# Run the app
uvicorn main:app --reload

# Navigate to http://localhost:8000/docs to see the auto-generated API docs.

```
