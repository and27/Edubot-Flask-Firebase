from flask import Blueprint

auth_b = Blueprint('auth', __name__, template_folder='templates')

from . import routes