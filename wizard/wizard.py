from odoo import models, fields,api

class ResCompany(models.TransientModel):
    _name = 'wizard'
   
    
    date_from=fields.Date()
    date_to=fields.Date()
    name=fields.Char()