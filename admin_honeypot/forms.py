'''
Forms for the admin_honeypot app.
'''
import django
from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm

class HoneypotLoginForm(AdminAuthenticationForm):
    '''
    Form to use for the fake admin login page.
    '''
    def clean(self):
        """
        Always raise the default error message, because we don't
        care what they entered here.
        """
        raise forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name}
        )
