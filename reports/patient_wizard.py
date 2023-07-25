import datetime

from odoo import models, fields,api,_




from datetime import date


class PatientData(models.AbstractModel):
    _name = "report.om_odoo.report_patient_wizard"


    @api.model
    def _get_report_values(self, docids, data=None):
        results = {}
        res1 = []
        for rec in self.env['patient.tag'].search([]):
            res1.append(rec)
        results['one'] = res1
        print(results)
        return {
            'doc_ids': docids,
            'data': results,
        }
