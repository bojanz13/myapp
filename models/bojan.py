# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class BojanApp(models.Model):
    _name = 'bojanova.aplikacija'
    _rec_name = 'ime'
    _description = 'Bojan App'

    ime = fields.Char(_("Ime"), required=True)
    prezime = fields.Char(_("Prezime"))
    broj_mob = fields.Char(string=_("Broj mobilnog"), required=True)
    broj_fix = fields.Char(string=_("Broj fiksnog"))
    slika = fields.Binary(string="Slika", attachment=True)

    @api.onchange('ime')
    def bojanva_metoda(self):
        i = self.ime
        if i:
            duzina = len(str(i))
            if duzina <= 2:
                raise UserError(_("Broj karaktera za ime mora biti veći od %s!!!.") % duzina)
            else:
                print(_("Drago mi je da ste uneli %s ime!!!.") % i)

    @api.onchange('broj_mob')
    def bojan_provera_br(self):
        mob = self.broj_mob
        if mob:
            if not mob.isdigit() and mob != False:
                raise UserError(_("Ovo nije dobar broj: %s!!!.") % mob)

