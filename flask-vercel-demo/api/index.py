from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello from Flask on Vercel!")

# Vercel needs a `handler` function to route requests
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
