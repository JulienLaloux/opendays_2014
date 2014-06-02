# -*- coding: utf-8 -*-
from openerp import Model
from openerp import Char, Integer

class teacher(Model):
    _name = "academy.ta"

    name = Char()
    age = Integer()
