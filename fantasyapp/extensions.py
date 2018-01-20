from flask_mail import Mail
from flask_wtf import CsrfProtect

mail = Mail()
csrf = CsrfProtect()
