# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    wsServer = fields.Char("WebSocket", help="The URL of your WebSocket",
                           default='ws://localhost', config_parameter='voip.wsServer')
    pbx_ip = fields.Char("PBX Server IP", help="The IP adress of your PBX Server",
                         default='localhost', config_parameter='voip.pbx_ip')
    mode = fields.Selection([
        ('demo', 'Demo'),
        ('prod', 'Production'),
    ], string="VoIP Environment", default='demo', config_parameter='voip.mode')
    # access_token = fields.Char(string='Access Token', config_parameter='voip.access.token')
    api_key_sid = fields.Char(string='API Key SID', config_parameter='voip.api.key.sid')
    api_key_secret = fields.Char(string='API Key Secret', config_parameter='voip.api.key.secret')
