from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello from Flask on Vercel!"}

# Needed for Vercel to find the app
def handler(request):
    return app(request.environ, start_response=lambda *args: None)
