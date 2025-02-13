from flask import Flask
from flask_cors import CORS
from controllers.customer_controller import customer_bp

app = Flask(__name__)

# Permitir solo el dominio de tu frontend
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Register Blueprint
app.register_blueprint(customer_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
