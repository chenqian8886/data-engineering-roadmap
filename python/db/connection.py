import psycopg

def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="sample_db",
        user="postgres",
        password="password"
    )