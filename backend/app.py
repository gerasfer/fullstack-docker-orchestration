from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Backend is Running!</h1><p>I am connected to the database.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
