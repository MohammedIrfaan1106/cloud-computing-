
import hashlib
from database import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Username: ")
    password = hash_password(input("Password: "))

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO users VALUES (?,?)", (username, password))
        conn.commit()
        print("Registration successful.")
    except:
        print("Username already exists.")
    conn.close()

def login_user():
    username = input("Username: ")
    password = hash_password(input("Password: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cur.fetchone()
    conn.close()

    if user:
        print("Login successful.")
        return username

    print("Invalid credentials.")
    return None
