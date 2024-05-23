from app import db
import logging

def check_database_connection():
    """
    Checks if the database connection is successful.
    """
    try:
        # Try to execute a simple query to check the connection
        db.session.execute('SELECT 1')
        logging.info("Database connection successful.")
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        raise e
