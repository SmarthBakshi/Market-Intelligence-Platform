.PHONY: help install dev build test clean docker-up docker-down lint format

help:
	@echo "Market Intelligence Platform - Available Commands"
	@echo ""
	@echo "Development:"
	@echo "  make install       Install all dependencies"
	@echo "  make dev           Start development servers"
	@echo "  make build         Build for production"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-up     Start all Docker services"
	@echo "  make docker-down   Stop all Docker services"
	@echo "  make docker-logs   View Docker logs"
	@echo ""
	@echo "Testing:"
	@echo "  make test          Run all tests"
	@echo "  make test-backend  Run backend tests"
	@echo "  make test-frontend Run frontend tests"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint          Run all linters"
	@echo "  make format        Format all code"
	@echo "  make type-check    Run type checkers"
	@echo ""
	@echo "Database:"
	@echo "  make db-migrate    Run database migrations"
	@echo "  make db-upgrade    Upgrade database"
	@echo "  make db-reset      Reset database"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean         Remove build artifacts"

# Installation
install: install-backend install-frontend

install-backend:
	cd backend && pip install -r requirements-dev.txt

install-frontend:
	cd frontend && npm install

# Development
dev:
	@echo "Starting development servers..."
	@echo "Backend will be at http://localhost:8000"
	@echo "Frontend will be at http://localhost:3000"
	@make -j2 dev-backend dev-frontend

dev-backend:
	cd backend && uvicorn app.main:app --reload

dev-frontend:
	cd frontend && npm run dev

# Build
build: build-backend build-frontend

build-backend:
	cd backend && docker build -t market-intel-backend .

build-frontend:
	cd frontend && npm run build

# Docker
docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-rebuild:
	docker-compose up -d --build

# Testing
test: test-backend test-frontend

test-backend:
	cd backend && pytest -v

test-frontend:
	cd frontend && npm test

test-coverage:
	cd backend && pytest --cov=app --cov-report=html
	cd frontend && npm run test:coverage

# Code Quality
lint: lint-backend lint-frontend

lint-backend:
	cd backend && flake8 app
	cd backend && mypy app

lint-frontend:
	cd frontend && npm run lint

format: format-backend format-frontend

format-backend:
	cd backend && black .
	cd backend && isort .

format-frontend:
	cd frontend && npm run format

type-check:
	cd backend && mypy app
	cd frontend && npm run type-check

# Database
db-migrate:
	cd backend && alembic revision --autogenerate -m "$(m)"

db-upgrade:
	cd backend && alembic upgrade head

db-downgrade:
	cd backend && alembic downgrade -1

db-reset:
	docker-compose down -v
	docker-compose up -d postgres
	sleep 5
	make db-upgrade

# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "node_modules" -exec rm -rf {} +
	find . -type d -name ".next" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +

# Pre-commit
pre-commit:
	make format
	make lint
	make test
