# Overview

This repository contains learning materials and practice code for Python and FastAPI development. The main project is a **Patient Management System API** built with FastAPI that demonstrates RESTful API concepts, path/query parameters, and JSON data handling. The repository also includes Python tutorials covering file operations (reading/writing text, JSON, and CSV files).

The FastAPI application serves as a simple patient records system with endpoints for viewing patient data, retrieving individual patient records by ID, and sorting patients based on health metrics (height, weight, BMI).

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## API Framework
- **FastAPI** is used as the web framework for building the REST API
- **ASGI (Asynchronous Server Gateway Interface)** architecture through Uvicorn server for async request handling
- **Pydantic** for data validation and type checking
- **Starlette** as the underlying framework for request/response handling

## Data Storage
- **JSON file-based storage** (`patients.json`) serves as the data source
- No database integration currently implemented
- Data is loaded into memory on each request using a `load_data()` helper function
- Patient records are keyed by patient IDs (e.g., "P001", "P002")

## API Design Patterns

### Endpoint Structure
1. **Root endpoint** (`/`) - Health check/welcome message
2. **View all patients** (`/view`) - Returns complete patient dataset
3. **View single patient** (`/view/{patient_id}`) - Path parameter for specific patient lookup
4. **Sort patients** (`/sort`) - Query parameters for sorting by metrics with ascending/descending order

### Error Handling
- **404 errors** for patient not found scenarios
- **400 errors** for invalid query parameters (invalid sort fields or sort order)
- HTTPException is used for standardized error responses

### Data Validation
- Path parameters use FastAPI's `Path()` with descriptions and examples
- Query parameters use `Query()` with validation for allowed values
- Valid sort fields are restricted to: 'height', 'weight', 'bmi'
- Sort order restricted to: 'asc', 'desc'

## Design Decisions

**JSON File Storage vs Database**: The current implementation uses JSON files for simplicity and learning purposes. This approach:
- **Pros**: Simple to understand, no setup required, human-readable
- **Cons**: Not scalable, no concurrent write support, entire dataset loaded per request
- **Future consideration**: Migration to a proper database (PostgreSQL/MongoDB) recommended for production

**Synchronous File I/O**: Uses standard Python file operations rather than async I/O
- **Rationale**: Simpler for learning; async file operations would be beneficial at scale

**In-memory sorting**: Patient sorting happens in application memory
- **Current approach**: Load all data, sort in Python
- **Alternative**: Database-level sorting would be more efficient for larger datasets

# External Dependencies

## Core Framework
- **FastAPI** - Modern Python web framework for building APIs
- **Uvicorn** - ASGI server for running the FastAPI application
- **Pydantic** - Data validation library (bundled with FastAPI)
- **Starlette** - ASGI framework (FastAPI dependency)

## Standard Library Dependencies
- **json** - For JSON file parsing and manipulation
- **csv** - For CSV file operations (in tutorials)

## Data Files
- **patients.json** - JSON data store containing patient records with fields:
  - Patient ID (key)
  - name, city, age, gender
  - height, weight, bmi, verdict (health classification)

## Future Integration Considerations
The repository notes indicate potential future integrations:
- **Machine Learning models** - To replace/augment database with ML predictions
- **Multiple frontend platforms** - Web, iOS, Android using the same API backend
- **Database migration** - Currently file-based; may add PostgreSQL or similar