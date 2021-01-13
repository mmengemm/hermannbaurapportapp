from flask import Blueprint, render_template	
from application import db
from application.forms import RapportForm

rapportBP = Blueprint('rapportBP',__name__, template_folder='templates')

@rapportBP.route('/rapport',methods=['GET','POST'])
def rapport():
    form = RapportForm()
    return render_template('rapport.html',form=form)