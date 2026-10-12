# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands
- Run application: `python app.py` (runs on port 5001)
- Install dependencies: `pip install -r requirements.txt` (if applicable)

## Architecture
Spendly is a Flask-based expense tracker application with a SQLite backend.

### Core Components
- `app.py`: Main entry point. Contains Flask application configuration, route definitions for authentication (login, register, logout), profile management, and expense CRUD operations.
- `database/db.py`: Database abstraction layer. Handles SQLite connections, table initialization (`init_db`), and provides a `get_db` helper for connection management.
- `templates/`: HTML templates for the frontend, using Jinja2. Includes base layout, landing page, auth pages, and expense management views.

### Data Model
- `users`: Stores user account information (username, email, password).
- `expenses`: Stores individual expense records linked to a user via `user_id` (foreign key).

### Key Flows
- **Authentication**: Session-based authentication using Flask `session`.
- **Expense Lifecycle**: Users can add, edit, and delete their own expenses, which are tracked in the `expenses` table and aggregated on the profile page.
