from flask import Blueprint, render_template	
from application import db

rapportBP = Blueprint('rapportBP',__name__, template_folder='templates')

@rapportBP.route('/rapport',methods=['GET','POST'])
def rapport():
    return render_template('rapport.html')