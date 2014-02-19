# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
from datetime import datetime

from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    cost = db.Column(db.String(12))
    date = db.Column(db.DateTime)

    def __init__(self, title='', cost='', date=None):
        self.title = title
        self.cost = cost
        if date is None:
            date = datetime.utcnow()
        self.date = date

    def __repr__(self):
        return '<Item %r>' % self.title

