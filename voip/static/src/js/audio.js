odoo.define('voip.PreviewContentAudio', function (require) {
"use strict";
    var core = require('web.core');
    var BasicFields= require('web.basic_fields');
    var FormController = require('web.FormController');
    var Registry = require('web.field_registry');
    var utils = require('web.utils');
    var session = require('web.session');
    var field_utils = require('web.field_utils');

    var _t = core._t;
    var QWeb = core.qweb;

    var FieldAudio = BasicFields.FieldChar.extend({
        template: 'voip.PreviewContentAudio',
        events: _.extend({}, BasicFields.FieldChar.prototype.events, {
            'click #smart_audio': '_on_click_play_audio',
        }),
    });
});
