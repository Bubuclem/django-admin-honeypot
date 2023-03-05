'''
App config for admin_honeypot app.
'''
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

__all__ = ['AdminHoneypotConfig']

class AdminHoneypotConfig(AppConfig):
    '''
    App config for admin_honeypot app.
    '''
    name = 'admin_honeypot'
    label = 'admin_honeypot'
    verbose_name = _('Admin Honeypot')
    default_auto_field = 'django.db.models.AutoField'
