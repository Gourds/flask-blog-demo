
from flask import Blueprint, render_template

mod = Blueprint('user', __name__, template_folder='templates')

@mod.route('/user')
def user():
    return render_template('user.html')