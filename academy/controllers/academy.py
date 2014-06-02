# -*- coding: utf-8 -*-

from openerp import http
from openerp.addons.web.controllers import main

# teaching_assistants = [
#     {'name': 'Joe', 'age': 18},
#     {'name': 'Ellen', 'age': 17},
#     {'name': 'Ed', 'age': 18},
# ]

class academy(main.Home):

    @http.route('/', auth='public', website=True)
    def index(self):
        cr, uid, context = http.request.cr, http.request.uid, http.request.context
        TAs = http.request.registry('academy.ta')
        tas = TAs.search_read(cr, uid, [], context=context)
        return http.request.render('academy.index', {'tas': tas})
        # return ''.join(
        #     '<li><a href="/tas/%d/">%s</a></li>' % (index, ta['name'])
        #     for index, ta in enumerate(teaching_assistants)
        # )

    @http.route('/tas/<int:index>/', auth='public', website=True)
    def ta(self, index):
        cr, uid, context = http.request.cr, http.request.uid, http.request.context
        TAs = http.request.registry('academy.ta')
        tas = TAs.read(cr, uid, index, context=context)
        return http.request.render('academy.ta', tas)
        # return "<p>%(name)s is %(age)d</p>" % teaching_assistants[index]
