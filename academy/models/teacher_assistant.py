# -*- coding: utf-8 -*-
from openerp import Model
from openerp import Char, Integer, Html, Boolean

class teacher(Model):
    _name = "academy.ta"

    name = Char()
    age = Integer()
    biography = Html()
    frontend_visible = Boolean()
