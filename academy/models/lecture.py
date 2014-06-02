# -*- coding: utf-8 -*-
from openerp import Model
from openerp import Char, Date

class Lecture(Model):
    _name = "academy.lecture"

    name = Char()
    date = Date()
