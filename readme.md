# FastAPI Refresher

A concise refresher for working with FastAPI. This document highlights core concepts and common commands to quickly get back up to speed.

## Overview
FastAPI is a modern, high-performance web framework for building APIs with Python 3.6+ using async support and Pydantic for data validation. This repo contains short examples and notes covering common patterns.

## Key Topics
- Creating routes (GET, POST, PUT, DELETE)
- Path, query, and body parameters
- Pydantic models and validation
- Dependency injection
- Background tasks and middleware
- Testing with TestClient
- Running and deploying with Uvicorn/Gunicorn

## Quick Start
1. Install poetry globally

    ```bash
        python3 -m pip install --user pipx
        pipx ensurepath
        pipx install poetry
    ```
2. Install dependencies:

    ```bash
        poetry install
    ```
3. Run the dev server:

    ```bash
    uvicorn main:app --reload
    ```

## Resources
- FastAPI docs: https://fastapi.tiangolo.com
- Pydantic docs: https://pydantic-docs.helpmanual.io

Keep examples small and focused; use this repo as a quick reference when you need a FastAPI refresher.
