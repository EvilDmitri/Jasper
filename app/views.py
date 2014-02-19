# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, models, db
from grabber.scrape import UltimateRewardsGrabber
from sqlalchemy.exc import OperationalError


def create_db():
    db.create_all()


@app.route('/')
def posts():

    try:
        items = models.Item.query.all()
    except OperationalError:
        create_db()
        items = ''
    return render_template('list.html', title='Rewards', items=items)


@app.route('/grab')
def add():
    # Grab data
    create_db()
    grabber = UltimateRewardsGrabber()
    grabber.grab()
    flash(u'Successfully grabbed')
    return 'OK'




