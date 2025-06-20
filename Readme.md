# Alembic = use for generate DB Migrations

# install commands alembic

1. poetry add pymongo fastapi python-dotenv alembic psycopg2-binary
2. poetry run alembic init alebic-postgress
3. poetry run alembic init

=> it handle our database migration

=> first connect it into DB
**Set the Database URL**

- Locate the `alembic.ini` file.
- Modify the `sqlalchemy.url` entry to point to your PostgreSQL database, e.g.:
  ```ini
  sqlalchemy.url = postgresql+psycopg2://user:password@localhost/dbname
  ```
