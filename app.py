from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import base64

app = Flask(__name__)
CORS(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Clipboard model
class Clipboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    content_type = db.Column(db.String(10), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/status934n2nfsdf', methods=['GET'])
def status():
    return jsonify({"status": "online"})

@app.route('/clipboard924kslfs', methods=['GET', 'POST', 'DELETE'])
def clipboard():
    if request.method == 'GET':
        items = Clipboard.query.all()
        return jsonify([{"id": item.id, "content": item.content, "content_type": item.content_type} for item in items])

    elif request.method == 'POST':
        data = request.json
        new_item = Clipboard(content=data['content'], content_type=data['content_type'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"id": new_item.id, "content": new_item.content, "content_type": new_item.content_type}), 201

    elif request.method == 'DELETE':
        item_id = request.args.get('id')
        item = Clipboard.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return '', 204
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)