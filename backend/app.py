from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/products')
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 999},
        {"id": 2, "name": "Phone", "price": 499}
    ])

app.run(host='0.0.0.0', port=5000)

