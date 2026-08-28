import sqlite3
from pydantic import BaseModel
DATABASE = "business.db"

class OrderInput(BaseModel):
    order_id: str
    customer: str
    status: str
    total: int


def init_db():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT UNIQUE NOT NULL,
            customer TEXT NOT NULL,
            status TEXT NOT NULL,
            total INTEGER NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT

        )
    
    """)

    connection.commit()

    connection.close()


def check_order(order_id):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM orders
        WHERE order_id = ?
    """, (order_id,))

    order = cursor.fetchone()

    connection.close()

    if order is None:
        return "Order not found"

    database_id, order_id, customer, status, total = order

    return {
        "order_id": order_id,
        "customer": customer,
        "status": status,
        "total": total
    }


def find_customer(customer):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT order_id, customer, status, total
        FROM orders
        WHERE customer = ?
    """, (customer,))

    orders = cursor.fetchall()

    connection.close()

    return [
        {
            "order_id": order[0],
            "customer": order[1],
            "status": order[2],
            "total": order[3]
        }
        for order in orders
    ]


def add_order(order_id, customer, status, total):

    order = OrderInput(
        order_id=order_id,
        customer=customer,
        status=status,
        total=total
    )

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO orders (order_id, customer, status, total)
            VALUES (?, ?, ?, ?)
        """, (
            order.order_id,
            order.customer,
            order.status,
            order.total
        ))

        connection.commit()

    except sqlite3.IntegrityError:

        connection.close()

        return "Order ID already exists"

    connection.close()

    return "Order created successfully"


def update_order(order_id, status):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE orders
        SET status = ?
        WHERE order_id = ?
    """, (status, order_id))

    connection.commit()

    if cursor.rowcount == 0:

        connection.close()

        return "Order not found"

    connection.close()

    return "Order updated successfully"


def cancel_order(order_id):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT status
        FROM orders
        WHERE order_id = ?
    """, (order_id,))

    order = cursor.fetchone()

    if order is None:

        connection.close()

        return "Order not found"

    status = order[0]

    if status == "Cancelled":

        connection.close()

        return "Order is already cancelled"

    if status != "Processing":

        connection.close()

        return f"Order cannot be cancelled because it is {status}"

    cursor.execute("""
        UPDATE orders
        SET status = ?
        WHERE order_id = ?
    """, ("Cancelled", order_id))

    connection.commit()

    connection.close()

    return "Order cancelled successfully"

def add_customer(name, email, phone):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO customers (name, email, phone)
        VALUES (?, ?, ?)

    """, (name, email, phone))

    connection.commit()
    connection.close()

    return "Customer created successfully"

init_db()
