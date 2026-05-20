import psycopg2

def connect():
    return psycopg2.connect(dbname="langchain", user="postgres", password="postgres", host="localhost", port="5432")

def insert_clients(firstname, surname, birth, gender, address, house_number, telephone, email):
    db_connection = connect()

    try:
        with db_connection.cursor() as cursor:
            cursor.execute("""INSERT INTO clients
                (
                    firstname,
                    surname,
                    birth,
                    gender,
                    address,
                    house_number,
                    telephone,
                    email
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING code""",
                (
                    firstname,
                    surname,
                    birth,
                    gender,
                    address,
                    house_number,
                    telephone,
                    email
                )
            )

            code = cursor.fetchone()[0]

            db_connection.commit()

            return code

    finally:
        db_connection.close()


def show_clients():
    db_connection = connect()

    try:
        with db_connection.cursor() as cursor:
            cursor.execute("""SELECT
                    code,
                    firstname,
                    surname,
                    birth,
                    gender,
                    address,
                    house_number,
                    telephone,
                    email,
                    register_date
                FROM clients
                ORDER BY firstname, surname""")
            return cursor.fetchall()

    finally:
        db_connection.close()


def search_client_code(code):
    db_connection = connect()

    try:
        with db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM clients WHERE code = %s",(code,))

            return cursor.fetchone()

    finally:
        db_connection.close()