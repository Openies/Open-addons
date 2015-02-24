# -*- coding: utf-'8' "-*-"

from openerp import models, fields, api, _


class CrmLead(models.Model):
    _inherit = "crm.lead"
    
    visible_tai_addr = fields.Boolean("Visible Taiwan Address")
    tw_street = fields.Many2one('res.street', ondelete='restrict', string='Street')
    tw_city = fields.Many2one('res.city', ondelete='restrict', string='City')
    tw_district_id = fields.Many2one("res.district", 'District', ondelete='restrict')
    country_id = fields.Many2one('res.country', 'Country', ondelete='restrict')
    show_address = fields.Boolean("Show Address")
    lane = fields.Integer("Lane")
    alley = fields.Integer("Alley")
    street_number = fields.Integer("Number")
    street_number2 = fields.Integer("Number2")
    floor = fields.Integer("Floor")
    floor2 = fields.Integer("Floor2")
    lane = fields.Integer("Lane")
    
    @api.onchange('country_id')
    def _country_id_changed(self):
        if self.country_id.name == 'Taiwan':
            self.visible_tai_addr = True
        else:
            self.visible_tai_addr = False
            
class ResPartner(models.Model):
    _inherit = "res.partner"


    visible_tai_addr = fields.Boolean("Visible Taiwan Address")
    tw_street = fields.Many2one('res.street', ondelete='restrict', string='Street')
    tw_city = fields.Many2one('res.city', ondelete='restrict', string='City')
    tw_district_id = fields.Many2one("res.district", 'District', ondelete='restrict')
    country_id = fields.Many2one('res.country', 'Country', ondelete='restrict')
    show_address = fields.Boolean("Show Address")
    lane = fields.Integer("Lane")
    alley = fields.Integer("Alley")
    street_number = fields.Integer("Number")
    street_number2 = fields.Integer("Number2")
    floor = fields.Integer("Floor")
    floor2 = fields.Integer("Floor2")
    lane = fields.Integer("Lane")

    @api.onchange('country_id')
    def _country_id_changed(self):
        if self.country_id.name == 'Taiwan':
            self.visible_tai_addr = True
        else:
            self.visible_tai_addr = False

class City(models.Model):
    _name = "res.city"

    code = fields.Char('Code')
    name = fields.Char('Name')
    country_id = fields.Many2one("res.country", string='State')

class District(models.Model):
    
    _name = "res.district"
    
    code = fields.Char('Code')
    name = fields.Char('Name')
    tw_city_id = fields.Many2one("res.city", string='State')

class Street(models.Model):
    _name = "res.street"

    code = fields.Char('Code')
    name = fields.Char('Name')
    tw_district_id = fields.Many2one("res.district", string='City')