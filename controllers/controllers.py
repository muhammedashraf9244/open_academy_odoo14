# -*- coding: utf-8 -*-
# from odoo import http


# class OpenAdacemyOdoo14(http.Controller):
#     @http.route('/open_academy_odoo14/open_academy_odoo14/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_academy_odoo14/open_academy_odoo14/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_academy_odoo14.listing', {
#             'root': '/open_academy_odoo14/open_academy_odoo14',
#             'objects': http.request.env['open_academy_odoo14.open_academy_odoo14'].search([]),
#         })

#     @http.route('/open_academy_odoo14/open_academy_odoo14/objects/<model("open_academy_odoo14.open_academy_odoo14"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_academy_odoo14.object', {
#             'object': obj
#         })
