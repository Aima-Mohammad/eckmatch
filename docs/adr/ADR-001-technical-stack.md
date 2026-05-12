# ADR-001 — Technical Stack

## Status

Accepted

---

## Context

EckMatch requires a modern, maintainable, secure, and scalable technology stack suitable for an internal enterprise platform handling regulatory reconciliation workflows.

The platform must support:

- secure data processing;
- matching workflows;
- auditability;
- fast development iteration;
- strong developer productivity;
- cloud deployment readiness.

---

## Decision

The project will use the following core stack:

### Frontend
- React
- TypeScript

### Backend
- Python
- FastAPI

### Database
- PostgreSQL

### Infrastructure
- Docker
- GitHub Actions

### Target Cloud
- Microsoft Azure

---

## Rationale

### React + TypeScript
Chosen for:
- strong ecosystem;
- maintainability;
- component architecture;
- enterprise adoption;
- typing safety.

### FastAPI
Chosen for:
- high productivity;
- strong typing;
- async support;
- automatic OpenAPI generation;
- excellent Python ecosystem integration.

### PostgreSQL
Chosen for:
- reliability;
- relational consistency;
- mature ecosystem;
- JSON support;
- strong enterprise adoption.

### Docker
Chosen for:
- reproducibility;
- environment consistency;
- deployment portability.

---

## Alternatives Considered

### Backend
- Django
- Node.js / NestJS
- Spring Boot

### Frontend
- Vue.js
- Angular

### Database
- MySQL
- MongoDB

---

## Consequences

### Positive
- Fast development velocity
- Strong maintainability
- Good scalability
- Excellent developer ecosystem
- Enterprise-ready architecture

### Negative
- Requires containerized local setup
- React ecosystem complexity
- Python runtime performance limitations for some workloads

---

## Decision Date

May 2026