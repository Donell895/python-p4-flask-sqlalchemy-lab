from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    def __repr__(self):
        return f'<Animal {self.name}, {self.species}>'

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)

    # Define the one-to-many relationship with Animal
    animals = db.relationship('Animal', backref='zookeeper', lazy='dynamic')

    def __repr__(self):
        return f'<Zookeeper {self.name}>'

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    # Define the one-to-many relationship with Animal
    animals = db.relationship('Animal', backref='enclosure', lazy='dynamic')

    def __repr__(self):
        return f'<Enclosure {self.environment}, Open to Visitors: {self.open_to_visitors}>'
