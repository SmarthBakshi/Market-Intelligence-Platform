# Market Intelligence Platform

> YouTube + Reddit Market Intelligence Platform - Transform videos and discussions into actionable business insights

## Overview

A scalable SaaS platform that automatically analyzes YouTube videos and Reddit discussions to extract pain points, trends, competitive insights, and messaging patterns for founders, product teams, and agencies.

## Key Features

- **Pain Point Extraction**: Automatically identify and cluster customer pain points
- **Competitor Analysis**: Track competitor messaging and identify gaps
- **Trend Detection**: Monitor emerging trends and shifting market dynamics
- **Messaging Insights**: Discover effective messaging patterns and common objections
- **Auto-Generated Reports**: Export insights as PDF or CSV, with shareable links

## Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL with async support
- **Vector DB**: Pinecone / Weaviate for embeddings
- **Cache/Queue**: Redis + Celery
- **ML/AI**: OpenAI GPT-4, Sentence Transformers

### Frontend
- **Framework**: Next.js 14 (React 18)
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Data Fetching**: TanStack Query
- **Forms**: React Hook Form + Zod

### Infrastructure
- **Containerization**: Docker & Docker Compose
- **Orchestration**: Kubernetes (production)
- **Cloud**: AWS / GCP (configurable)
- **CI/CD**: GitHub Actions

## Project Structure

```
Market-Intelligence/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── core/           # Core utilities (config, security, logging)
│   │   ├── db/             # Database configuration
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Business logic (YouTube, Reddit, ML)
│   │   ├── ml/             # ML components (embeddings, clustering)
│   │   └── utils/          # Utility functions
│   ├── tests/              # Test suite
│   ├── scripts/            # Utility scripts
│   └── requirements.txt    # Python dependencies
├── frontend/               # Next.js frontend
│   ├── src/
│   │   ├── app/           # Next.js app directory
│   │   ├── components/    # React components
│   │   ├── lib/           # Utilities and configurations
│   │   ├── hooks/         # Custom React hooks
│   │   ├── services/      # API services
│   │   └── types/         # TypeScript types
│   └── public/            # Static assets
├── infrastructure/         # Infrastructure as Code
│   ├── docker/            # Docker configurations
│   ├── kubernetes/        # K8s manifests
│   └── terraform/         # Terraform configs
├── scripts/               # Project scripts
├── Docs/                  # Documentation
└── docker-compose.yml     # Local development setup
```

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 20+
- Docker & Docker Compose
- PostgreSQL 16+
- Redis 7+

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Market-Intelligence
   ```

2. **Backend Setup**
   ```bash
   cd backend
   cp .env.example .env
   # Edit .env with your API keys

   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements-dev.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   cp .env.example .env.local
   # Edit .env.local with your configuration

   # Install dependencies
   npm install
   ```

4. **Start Services with Docker Compose**
   ```bash
   # From project root
   docker-compose up -d postgres redis weaviate
   ```

5. **Run Backend**
   ```bash
   cd backend
   uvicorn app.main:app --reload
   # API available at http://localhost:8000
   # API docs at http://localhost:8000/api/v1/docs
   ```

6. **Run Frontend**
   ```bash
   cd frontend
   npm run dev
   # Frontend available at http://localhost:3000
   ```

### Using Docker Compose (Full Stack)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild services
docker-compose up -d --build
```

## Configuration

### Backend Configuration

See `backend/.env.example` for all available configuration options:
- Database connection
- API keys (YouTube, Reddit, OpenAI)
- Vector database settings
- Feature flags
- Rate limits

### Frontend Configuration

See `frontend/.env.example` for frontend configuration:
- API endpoint
- Feature flags
- Analytics configuration

## API Documentation

Once the backend is running, visit:
- Swagger UI: `http://localhost:8000/api/v1/docs`
- ReDoc: `http://localhost:8000/api/v1/redoc`

## Testing

### Backend Tests
```bash
cd backend
pytest
pytest --cov=app --cov-report=html
```

### Frontend Tests
```bash
cd frontend
npm test
npm run test:coverage
```

## Code Quality

### Backend
```bash
cd backend
black .                    # Format code
isort .                    # Sort imports
flake8                     # Lint
mypy app                   # Type check
```

### Frontend
```bash
cd frontend
npm run lint               # Lint
npm run format             # Format with Prettier
npm run type-check         # TypeScript check
```

## Deployment

### Production Build

**Backend:**
```bash
cd backend
docker build -t market-intel-backend --target production .
```

**Frontend:**
```bash
cd frontend
npm run build
docker build -t market-intel-frontend --target production .
```

### Environment Variables

Ensure all production environment variables are set:
- Database credentials
- API keys
- Secret keys (use strong, unique values)
- CORS origins
- Monitoring/logging services

## Architecture

### Data Flow
1. User inputs YouTube channels/videos or Reddit subreddits
2. Background jobs fetch and process content
3. ML pipeline extracts embeddings and insights
4. Results stored in PostgreSQL + Vector DB
5. Frontend displays structured insights and reports

### Scalability
- Async I/O for API endpoints
- Background job processing with Celery
- Database connection pooling
- Redis caching layer
- Horizontal scaling via Kubernetes

## Contributing

1. Create a feature branch (`git checkout -b feature/amazing-feature`)
2. Make your changes
3. Run tests and linters
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

Proprietary - All rights reserved

## Support

For issues and questions:
- Create an issue in the repository
- Contact: [your-email@example.com]

---

Built with ❤️ for founders, PMs, and agencies
