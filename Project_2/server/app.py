from flask import Flask
from flask_cors import CORS
from blueprints.auth_blueprint import auth_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp)  # Register the blueprint

if __name__ == '__main__':
    app.run(debug=True)