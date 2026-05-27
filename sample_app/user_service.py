import requests
import sqlite3

# Simulated DB connection
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (email TEXT, name TEXT, phone TEXT)")


def register_user(data):
    """Registers a new user — personal data flows to API and DB."""
    user_email = data["email"]
    user_name = data["name"]
    phone = data["phone"]

    # SINK: personal data sent to external API
    requests.post("https://api.example.com/users", json={
        "email": user_email,
        "name": user_name
    })

    # SINK: personal data written to database
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (user_email, user_name, phone))
    conn.commit()


def send_welcome_email(user_email, user_name):
    """Sends a welcome email — another sink."""
    payload = {"to": user_email, "body": f"Welcome, {user_name}!"}

    # SINK: email dispatch
    requests.post("https://mail.example.com/send", json=payload)


def log_access(ip_address, user_id):
    """Logs access — IP and user ID are personal data."""
    # SINK: logging personal data
    print(f"Access from {ip_address} by user {user_id}")

    cursor.execute("INSERT INTO access_log VALUES (?, ?)", (ip_address, user_id))
    conn.commit()


if __name__ == "__main__":
    register_user({
        "email": "parth@example.com",
        "name": "Parth Dhamdhere",
        "phone": "+91-7776977939"
    })
    send_welcome_email("parth@example.com", "Parth")
    log_access("192.168.1.1", "user_42")
