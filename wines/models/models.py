from flectra import models, fields, api


class SzoloAtvetel(models.Model):
    _name = 'wines.szoloatvet'

    #name = fields.Integer(string="Szőlőfajta")
    name= fields.Selection(selection=[(1, 'Irsai Olivér'),
                                      (2, 'Cserszegi fűszeres'),
                                      (3, 'Ezerjó'),
                                      (4, 'Generoa'),
                                      (5, 'Hibernál'),
                                      (6, 'Kunleány'),
                                      (7, 'Kövidinka'),
                                      (8, 'Bianka'),
                                      (9, 'Kékfrankos'),
                                      (10, 'Portugiser'),
                                      (11, 'Merlot'),
                                      (12, 'Cabernet S'),
                                      (13, 'Cabernet F'),
                                      (14, 'Kadaka'),
                                      (15, 'Zweigelt'),
                                      (16, 'Medina'),
                                      (17, 'Néró'),
                                      (18, 'Pinot Noir'),
                                      (19, 'Sauvignon Blanc'),
                                      (20, 'Rajni R'),], string="Szőlőfajta")

    mazsajegy = fields.Integer(string="Mázsajegy szám")
    amount = fields.Many2one('stock.quant_quantity', ondelete="cascade", string="Mennyiség", required=True)
    quality = fields.Selection(selection=[(1, '1'),
                                          (2, '2'),
                                          (3, '3'),
                                          (4, '4'),
                                          (5, '5'),], string='Minőség')
    mustfok = fields.Integer(string="Mustfok % M/M")
    #vendor = fields.Char(string="Beszállító")
    vendor = fields.Many2one('res.partner', ondelete='set null', string="Beszállító")
    addon = fields.Char(string="Segédanyag")
    description = fields.Char(string="Megjegyzés")