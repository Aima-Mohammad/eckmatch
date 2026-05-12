# EckMatch

Internal matching platform for regulatory death-to-member reconciliation workflows.

---

## Overview

EckMatch is an internal enterprise platform designed to support regulatory workflows related to deceased insured members, beneficiary identification, and contract reconciliation.

The platform helps operational teams:

- ingest weekly member datasets;
- process death notification datasets;
- automatically match deceased persons with internal member records;
- review and validate potential matches;
- track decisions and audit history;
- generate operational and regulatory reporting.

---

## Business Context

The project is designed around insurance regulatory obligations related to unclaimed contracts and beneficiary identification workflows.

EckMatch aims to industrialize and secure reconciliation operations while improving:

- operational efficiency;
- traceability;
- auditability;
- matching reliability;
- regulatory compliance.

---

## Core Features

- Weekly member snapshot ingestion
- Death notification ingestion
- Automated matching engine
- Match scoring & explainability
- Human review workflow
- Audit trail
- Reporting dashboard
- Regulatory KPIs
- Role-based access control

---

## Architecture

```text
Frontend (React + TypeScript)
        ↓
Backend API (FastAPI)
        ↓
PostgreSQL Database
        ↓
Secure Storage & Processing Pipelines
```

---

## Tech Stack

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
- Azure (target)

---

## Repository Structure

```text
frontend/     → React application
backend/      → FastAPI backend
infra/        → infrastructure & deployment
docs/         → project documentation
datasets/     → synthetic datasets
tests/        → automated tests
scripts/      → helper scripts
```

---

## Documentation

Project documentation is available in `/docs`.

Main documents:

- Product Requirements Document (PRD)
- Architecture Decision Records (ADR)
- Technical Architecture
- API Documentation

---

## Project Status

Current phase:

> Product architecture & platform foundation

---

## Roadmap

### Phase 1
- Repository setup
- Architecture foundations
- Backend bootstrap
- Frontend bootstrap

### Phase 2
- Data ingestion pipelines
- Matching engine
- Review workflow

### Phase 3
- Reporting
- Security hardening
- Cloud deployment

---

## Security & Privacy

EckMatch is designed with:

- privacy by design;
- security by design;
- role-based access control;
- auditability;
- data minimization principles.

Sensitive personal identifiers are intentionally excluded from long-term storage.

---

## License

MIT