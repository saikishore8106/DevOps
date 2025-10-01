from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to MySQL database
    connection = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "db"),
        user="root",
        password="root",
        database="testdb"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT 'Hello from Flask + MySQL!'")
    result = cursor.fetchone()
    return result[0]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

