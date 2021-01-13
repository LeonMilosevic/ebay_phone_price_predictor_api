import psycopg2

def database_connect(database: str, user: str, password: str, host: str, port: str) -> None:
    return psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port
    )

# try:
#     cursor = db_connection.cursor()
#     cursor.execute(
#         '''CREATE TABLE predictions (
#             id serial PRIMARY KEY,
#             brand varchar(255),
#             ram numeric,
#             storage numeric,
#             processor numeric,
#             camera numeric,
#             condition varchar(32),
#             evaluation numeric
#         )
#         '''
#     )
#     db_connection.commit()
#     cursor.close()
# except:
#     cursor.close()
