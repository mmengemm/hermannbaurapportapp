"""
author: Melanie Menge
date: 2020-09-02

description: database models
"""
from . import db
from flask_login import UserMixin


class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'login'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )
    username = db.Column(
        db.String(45),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )
    admin = db.Column(
        db.Boolean,
        nullable=False
    )
    password = db.Column(
        db.String(150),
        nullable=False
    )
    salt = db.Column(
        db.String(10),
        nullable=False
    )
    active = db.Column(
        db.Boolean,
        nullable=False
    )

    def is_authenticated(bool):
        return bool
    
    def is_active():
        return User.active

    def get_id():
        return User.id

class Plz(db.Model):
    """Data model for postcodes"""

    __tablename__ = 'plz'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )
    plz = db.Column(
        db.String(10),
        nullable=False,
        unique=True
    )
    ort = db.relationship(
        'Ort',
        backref='plz',
        lazy=True
    )



class Ort(db.Model):
    """Data model for towns"""

    __tablename__ = 'ort'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )
    ort = db.Column(
        db.String(45),
        nullable=False,
        unique=True
    )
    fk_plz = db.Column(
        db.Integer,
        db.ForeignKey('plz.id')
    )
    kunde = db.relationship(
        'Kunde',
        backref='ort',
        lazy=True
    )
    baustelle = db.relationship(
        'Baustelle',
        backref='ort',
        lazy=True
    )
    mitarbeiter = db.relationship(
        'Mitarbeiter',
        backref='ort',
        lazy=True
    )


class Kunde(db.Model):
    """Data model for clients."""

    __tablename__ = 'kunden'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )
    firma = db.Column(
        db.String(45),
        unique=True,
        nullable=False
    )
    ansprechsperson = db.Column(
        db.String(45),
        nullable=True
    )
    adresse = db.Column(
        db.String(100),
        nullable=False
    )
    plzort = db.Column(
        db.Integer,
        db.ForeignKey('ort.id')
    )
    email = db.Column(
        db.String(50),
        nullable=False
    )
    baustelle = db.relationship(
        'Baustelle',
        backref='kunden',
        lazy=True
    )
    rapport = db.relationship(
        'Rapport',
        backref='kunden',
        lazy=True
    )


class Baustelle(db.Model):
    """Data model for building sites"""

    __tablename__ = 'baustellen'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )
    baustelle = db.Column(
        db.String(45),
        nullable=False,
        unique=True
    )
    fk_kunde = db.Column(
        db.Integer,
        db.ForeignKey('kunden.id')
    )
    adresse = db.Column(
        db.String(100),
        nullable=False
    )
    fk_ort = db.Column(
        db.Integer,
        db.ForeignKey('ort.id')
    )
    rapport = db.relationship(
        'Rapport',
        backref='baustellen',
        lazy=True
    )


class Rapport(db.Model):
    """Data model for reports"""

    __tablename__ = 'rapport'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )
    fk_mitarbeiter = db.Column(
        db.Integer,
        db.ForeignKey('mitarbeiter.id'),
        nullable=False
    )
    fk_kunde = db.Column(
        db.Integer,
        db.ForeignKey('kunden.id'),
        nullable=False
    )
    fk_baustelle = db.Column(
        db.Integer,
        db.ForeignKey('baustellen.id'),
        nullable=False
    )
    datum = db.Column(
        db.Date,
        nullable=False
    )
    stunden = db.Column(
        db.Float,
        nullable=False
    )
    arbeit = db.Column(
        db.Text,
        nullable=False
    )
    signature = db.Column(
        db.Text,
        nullable=False
    )


class Mitarbeiter(db.Model):
    """Data model for workers"""

    __tablename__ = 'mitarbeiter'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )
    vorname = db.Column(
        db.String(45),
        nullable=False
    )
    nachname = db.Column(
        db.String(45),
        nullable=False
    )
    adresse = db.Column(
        db.String(100),
        nullable=False
    )
    email = db.Column(
        db.String(45),
        nullable=False,
        unique=True
    )
    fk_ort = db.Column(
        db.Integer,
        db.ForeignKey('ort.id'),
        nullable=False
    )
    ahv = db.Column(
        db.String(45),
        nullable=False,
        unique=True
    )
    telnr = db.Column(
        db.String(45),
        nullable=False
    )
    gebdat = db.Column(
        db.Date,
        nullable=False
    )
    rapport = db.relationship(
        'Rapport',
        backref='mitarbeiter',
        lazy=True
    )

