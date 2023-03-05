'''
File to define signals for the admin_honeypot app.
'''
from django import dispatch

honeypot = dispatch.Signal()
