#!/usr/bin/env python3

from flask import Flask, render_template
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    # Query the database to get the animal by ID
    animal = Animal.query.get(id)
    
    if animal:
        return render_template('animal.html', animal=animal)
    else:
        return 'Animal not found', 404

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    # Query the database to get the zookeeper by ID
    zookeeper = Zookeeper.query.get(id)
    
    if zookeeper:
        return render_template('zookeeper.html', zookeeper=zookeeper)
    else:
        return 'Zookeeper not found', 404

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    # Query the database to get the enclosure by ID
    enclosure = Enclosure.query.get(id)
    
    if enclosure:
        return render_template('enclosure.html', enclosure=enclosure)
    else:
        return 'Enclosure not found', 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
