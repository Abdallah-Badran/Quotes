from flask import Flask, render_template
from routes.quotes import quotes_routes
# from flask_cors import CORS


app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(quotes_routes)


@app.get('/')
def home():
    return render_template('./index.html')

