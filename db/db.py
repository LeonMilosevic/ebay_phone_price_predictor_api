import psycopg2

def database_connect(database: str, user: str, password: str, host: str, port: str) -> None:
    return psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port
    )