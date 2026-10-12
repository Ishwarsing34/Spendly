---
description: Seed the database with dummy data for development and testing
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
---

# Seed Database with Dummy Data

Seed the project's database with realistic dummy data for development and testing.

## Instructions

1. Inspect the project structure and identify the database, ORM, and existing database schema.
2. Read the relevant schema, models, migrations, and existing seed scripts to understand the database structure and relationships.
3. Check `package.json` or the project's configuration files to identify the existing database seeding commands and dependencies.
4. Generate realistic, consistent dummy data that follows the schema, validation rules, and relationships between tables or collections.
5. Prefer the project's existing seed script and data-generation utilities. If no seed script exists, create one that follows the project's existing conventions.
6. Ensure related records reference valid IDs and required fields are populated.
7. Use deterministic or appropriately generated dummy values where practical, and avoid inserting duplicate records when the command is run repeatedly.
8. Execute the seed script using the project's existing commands, provided the database is configured and accessible.
9. Verify that the seeding process completes successfully and report the records created.

## Safety Rules

- Never delete existing data, drop tables, reset the database, or run destructive migrations.
- Never modify production data or connect to a production database for seeding.
- Inspect the database connection configuration and confirm the target is a development or test database before writing data.
- Never expose database credentials, API keys, or other secrets.
- Do not invent schema fields or bypass existing validation constraints.
- If the database environment is ambiguous, or the target cannot be confirmed as development or test, stop and ask for clarification.

## Final Output

Report:
- The database and seeding approach used.
- The tables or collections populated.
- The number of records created for each.
- The command used to execute the seed script.
- Any errors or manual steps required.