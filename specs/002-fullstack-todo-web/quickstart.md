# Quickstart Guide: Phase 2 Full-Stack Todo Web Application

**Feature**: 002-fullstack-todo-web
**Date**: 2025-12-29

---

## Prerequisites

### Required Software
- **Node.js** 18+ (for frontend)
- **Python** 3.11+ (for backend)
- **Git** (version control)

### Required Accounts
- **Neon** account (free tier available) - [neon.tech](https://neon.tech)
- **Vercel** account (for frontend deployment) - [vercel.com](https://vercel.com)

---

## Project Structure

```
todo-app-hackathon2/
├── frontend/                 # Next.js application
│   ├── app/                  # App Router pages
│   ├── components/           # React components
│   ├── lib/                  # Utilities and API client
│   ├── package.json
│   └── .env.local            # Frontend environment variables
│
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── main.py           # FastAPI entry point
│   │   ├── models/           # SQLModel database models
│   │   ├── routers/          # API route handlers
│   │   ├── services/         # Business logic
│   │   └── core/             # Config, security, dependencies
│   ├── tests/                # pytest tests
│   ├── requirements.txt
│   └── .env                  # Backend environment variables
│
├── specs/                    # Specifications (this folder)
└── .specify/                 # Constitution and templates
```

---

## Setup Instructions

### 1. Clone and Navigate

```bash
git clone <repository-url>
cd todo-app-hackathon2
git checkout 002-fullstack-todo-web
```

### 2. Setup Neon Database

1. Create account at [neon.tech](https://neon.tech)
2. Create new project (e.g., "todo-phase2")
3. Copy the connection string (pooled)
4. Note: Connection string format:
   ```
   postgresql://<user>:<password>@<host>/<database>?sslmode=require
   ```

### 3. Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env with your values:
# DATABASE_URL=postgresql+asyncpg://<user>:<password>@<host>/<database>?sslmode=require
# JWT_SECRET=<your-secret-key-min-32-chars>
# JWT_ALGORITHM=HS256
# CORS_ORIGINS=http://localhost:3000

# Run database migrations (when implemented)
# alembic upgrade head

# Start development server
uvicorn app.main:app --reload --port 8000
```

Backend will be available at: `http://localhost:8000`
API docs at: `http://localhost:8000/docs`

### 4. Frontend Setup

```bash
# Navigate to frontend (from project root)
cd frontend

# Install dependencies
npm install

# Create .env.local file
cp .env.example .env.local

# Edit .env.local with your values:
# NEXT_PUBLIC_API_URL=http://localhost:8000/api
# BETTER_AUTH_SECRET=<same-secret-as-backend>

# Start development server
npm run dev
```

Frontend will be available at: `http://localhost:3000`

---

## Environment Variables

### Backend (.env)

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | Neon PostgreSQL connection (asyncpg) | `postgresql+asyncpg://user:pass@host/db?sslmode=require` |
| `JWT_SECRET` | Secret key for JWT validation | `your-super-secret-key-min-32-characters` |
| `JWT_ALGORITHM` | JWT signing algorithm | `HS256` |
| `CORS_ORIGINS` | Allowed frontend origins | `http://localhost:3000,https://yourapp.vercel.app` |

### Frontend (.env.local)

| Variable | Description | Example |
|----------|-------------|---------|
| `NEXT_PUBLIC_API_URL` | Backend API base URL | `http://localhost:8000/api` |
| `BETTER_AUTH_SECRET` | Secret for Better Auth (same as backend) | `your-super-secret-key-min-32-characters` |

---

## Development Workflow

### Running Both Services

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn app.main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Testing

**Backend Tests:**
```bash
cd backend
pytest
```

**Frontend Tests:**
```bash
cd frontend
npm test
```

---

## API Endpoints Quick Reference

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/auth/register` | Register new user | No |
| POST | `/api/auth/login` | Login user | No |
| POST | `/api/auth/logout` | Logout user | Yes |
| GET | `/api/tasks` | List user's tasks | Yes |
| POST | `/api/tasks` | Create new task | Yes |
| GET | `/api/tasks/{id}` | Get single task | Yes |
| PUT | `/api/tasks/{id}` | Update task | Yes |
| DELETE | `/api/tasks/{id}` | Delete task | Yes |
| PATCH | `/api/tasks/{id}/complete` | Toggle completion | Yes |

---

## Deployment

### Frontend (Vercel)

1. Push code to GitHub
2. Connect repository to Vercel
3. Set environment variables in Vercel dashboard:
   - `NEXT_PUBLIC_API_URL` = your backend production URL
   - `BETTER_AUTH_SECRET` = your secret key
4. Deploy

### Backend (Railway/Render/Fly.io)

1. Push code to GitHub
2. Connect repository to hosting platform
3. Set environment variables:
   - `DATABASE_URL` = Neon production connection string
   - `JWT_SECRET` = your secret key
   - `JWT_ALGORITHM` = HS256
   - `CORS_ORIGINS` = your Vercel frontend URL
4. Deploy

---

## Common Issues

### CORS Errors
- Ensure `CORS_ORIGINS` includes your frontend URL
- Check both development and production URLs

### Database Connection Failed
- Verify Neon connection string format
- Ensure `?sslmode=require` is included
- Check if Neon project is active (free tier pauses after inactivity)

### JWT Token Invalid
- Ensure `JWT_SECRET` matches between frontend and backend
- Check token expiration settings

### Frontend API Calls Failing
- Verify `NEXT_PUBLIC_API_URL` points to correct backend
- Check browser console for detailed errors

---

## Next Steps After Setup

1. Run `/sp.tasks` to generate implementation tasks
2. Follow task order (backend first, then frontend)
3. Test each endpoint as implemented
4. Deploy to staging environment
5. Run acceptance tests against deployment
