#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# forms.py

from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, BooleanField, FieldList
from wtforms import SelectField, FormField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'

class OdpForm(FlaskForm):
    id = HiddenField()
    pytanie = HiddenField()
    odpowiedz = StringField('Odpowiedź: ', validators = [Required(message = blad1)])
    odpok = BooleanField('Poprawna: ')
    
class DodajForm(FlaskForm):
    pytanie = StringField('Pytanie: ', validators = [Required(message = blad1)])
    kategorie = SelectField('Kategoria: ', coerce = int)
    odpowiedzi = FieldList(FormField(OdpForm), min_entries = 3)
