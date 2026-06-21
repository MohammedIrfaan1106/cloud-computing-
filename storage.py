
import os, shutil
from database import get_connection

UPLOAD_DIR = "cloud_storage/uploads"

def upload_file(username):
    path = input("Enter file path: ")
    if not os.path.exists(path):
        print("File not found.")
        return

    filename = os.path.basename(path)
    dest = os.path.join(UPLOAD_DIR, filename)

    shutil.copy(path, dest)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO files(username,filename,filepath) VALUES (?,?,?)",
                (username, filename, dest))
    conn.commit()
    conn.close()

    print("File uploaded.")

def list_files(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT filename FROM files WHERE username=?", (username,))
    rows = cur.fetchall()
    conn.close()

    for r in rows:
        print(r[0])

def delete_file(username):
    filename = input("File name: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT filepath FROM files WHERE username=? AND filename=?",
                (username, filename))
    row = cur.fetchone()

    if row:
        if os.path.exists(row[0]):
            os.remove(row[0])
        cur.execute("DELETE FROM files WHERE username=? AND filename=?",
                    (username, filename))
        conn.commit()
        print("Deleted.")
    else:
        print("File not found.")

    conn.close()

def search_file(username):
    keyword = input("Search: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT filename FROM files WHERE username=? AND filename LIKE ?",
                (username, f"%{keyword}%"))
    rows = cur.fetchall()
    conn.close()

    for r in rows:
        print(r[0])

def storage_usage(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT filepath FROM files WHERE username=?", (username,))
    rows = cur.fetchall()
    conn.close()

    total = 0
    for r in rows:
        if os.path.exists(r[0]):
            total += os.path.getsize(r[0])

    print(f"Storage Used: {total/1024:.2f} KB")
