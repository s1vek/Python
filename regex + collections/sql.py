def insert_post (nickname, text):
    if not nickname or not text:
        raise ValueError("Error")

    sql_query = f"INSERT INTO PRISPEVEK (AUTHOR, TEXT) VALUES ('{nickname}', '{text}');"

    return sql_query


nickname = "JanNovak"
text = "Commit"
sql_command = insert_post(nickname, text)

print(sql_command)

def number_change (username, number):
    if len(number) != 9 or not number.isdigit():
        raise ValueError("Error")

    query = "UPDATE USER SET NUMBER = %s WHERE USERNAME = %s;"



def change_email (username, email):
    if len(email) < 100 and len(username) < 255:
        raise ValueError("Error")

    query = "UPDATE USER SET EMAIL = %s WHERE USERNAME = %s;"

