# -*- coding: utf-8 -*-
from flectra import http

# class Wines(http.Controller):
#     @http.route('/wines/wines/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wines/wines/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wines.listing', {
#             'root': '/wines/wines',
#             'objects': http.request.env['wines.wines'].search([]),
#         })

#     @http.route('/wines/wines/objects/<model("wines.wines"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wines.object', {
#             'object': obj
#         })