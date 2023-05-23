from flask import BluePrint

task = Blueprint('task', __name__, template_folder='templates')

from . import views
