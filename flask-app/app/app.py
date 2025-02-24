from flask import Flask
import redis
import os

app = Flask(__name__)
cache = redis.Redis(host='redis-service', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = cache.incr('visits')
    return f"Hello, World! Page visited {count} times."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
