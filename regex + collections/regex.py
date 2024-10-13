import re
from re import search


def password_policy_check (username, password):

    if len(password) <= 10:
        return "Password must be at least 10 characters"

    if not re.search(r'\d', password):
        return "Password must contain at least one number"

    if not re.search(r'[a-z]', password):
        return "Password must contain at least one letter"
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter"

    if not re.search(r'\W', password):
        return "Invalid"
    if not re.search(r'\D', password):
        return "Invalid"

    if password == username:
        return "Password shouldnt be matching username"




print(password_policy_check("zden", "helloHellohello1@"))
print(password_policy_check("zdenZdenzden1@", "zdenZdenzden1@"))