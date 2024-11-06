from odoo import models, fields, api
import os

class LogRestore(models.Model):
    _name = 'excise.log.restore'
    _description = 'Logs containing the word restore'

    log_line = fields.Text(string="Log Line")

    @api.model
    def fetch_restore_logs(self):
        log_file_path = '/var/log/odoo/odoo-server.log'
        restore_logs = []

        if os.path.exists(log_file_path):
            with open(log_file_path, 'r') as f:
                for line in f:
                    if 'restore' in line.lower():
                        restore_logs.append({'log_line': line.strip()})
        
        # Create log entries
        self.create(restore_logs)

        return True

    def action_fetch_logs(self):
        self.fetch_restore_logs()
        return True