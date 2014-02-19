# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask.ext.wtf import Form, TextField, DateTimeField
from flask.ext.wtf import Required


class ExampleForm(Form):
    title = TextField(u'Name', validators=[Required()])
    content = TextField(u'Rate')
    date = DateTimeField(u'Data', format='%d/%m/%Y %H:%M')



