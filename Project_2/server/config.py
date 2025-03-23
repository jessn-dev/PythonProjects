import psycopg2
import os

# Database configuration (using environment variables for security)
DB_HOST = os.environ.get("DB_HOST", "localhost")  # Default to localhost
DB_NAME = os.environ.get("DB_NAME", "your_db_name")
DB_USER = os.environ.get("DB_USER", "your_db_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "your_db_password")
DB_PORT = os.environ.get("DB_PORT", "5432") # Default PostgreSQL port

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}") # Log the error for debugging
        return None  # Return None if connection fails