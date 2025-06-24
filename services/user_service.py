from db.database import get_connection
from schemas.user import UserCreate, UserUpdate

def create_user(user: UserCreate):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.email))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, name, email FROM users")

        rows = cur.fetchall()
        return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]
    finally:
        cur.close()
        conn.close()

def update_user(user_id: int, user: UserUpdate):
    conn = get_connection()
    cur = conn.cursor()
    try:
        query = "UPDATE users SET "
        params = []
        if user.name:
            query += "name = %s, "
            params.append(user.name)
        if user.email:
            query += "email = %s, "
            params.append(user.email)
        query = query.rstrip(", ") + " WHERE id = %s"
        params.append(user_id)
        cur.execute(query, tuple(params))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def delete_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
    finally:
        cur.close()
        conn.close()
