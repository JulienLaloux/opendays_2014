# -*- coding: utf-8 -*-

from openerp import http
from openerp.addons.web.controllers import main

class academy(main.Home):

    @http.route('/', auth='public', website=True)
    def index(self):
        cr, uid, context = http.request.cr, http.request.uid, http.request.context
        TAs = http.request.registry('academy.ta')
        tas = TAs.search_read(cr, uid, [], context=context)
        return http.request.render('academy.index', {'tas': tas})

    ## The name after the 2 points must be the same same as in the function call. Keyword must be the same
    @http.route('/tas/<model("academy.ta"):record>/', auth='public', website=True)
    def ta(self, record):
        return http.request.render('academy.ta', {'ta': record})
