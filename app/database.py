import sqlite3
connection = sqlite3.connect(
    "chat.db",
    check_same_thread=False
)

cursor = connection.cursor()
def create_conversation():
    cursor.execute("INSERT INTO conversations DEFAULT VALUES")
    connection.commit()

    return cursor.lastrowid
def get_conversations():
    cursor.execute("""
        SELECT id, created_at
        FROM conversations
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    return [
        {
            "id": rows[0],
            "created_at": rows[1]

        }
        for rows in rows
    ]
def get_messages(conversation_id):
    cursor.execute(
        "SELECT role, content FROM messages WHERE conversation_id = ?",
        (conversation_id,)
    )
    rows =  cursor.fetchall()
    return [
    {
        "role": row[0],
        "content": row[1]
    }
    for row in rows
]
def save_message(conversation_id, role, content):
    cursor.execute(
        """
        INSERT INTO messages (conversation_id, role, content)
        VALUES (?,?,?)
        """,
        (conversation_id, role, content)
    )

    connection.commit()
    
cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id)
)
""")

connection.commit()

def delete_conversation(conversation_id):
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM messages WHERE conversation_id = ?",
        (conversation_id,)
    )

    cursor.execute(
        "DELETE FROM conversations WHERE id = ?",
        (conversation_id,)
    )

    connection.commit()

    cursor.close()


