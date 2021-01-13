from flask import Blueprint, render_template	
from flask_login import login_required, roles_required
from application import db

admin = Blueprint('admin',__name__, template_folder='templates')

@admin.route('/admin', methods=['GET','POST'])
@login_required
@roles_required('admin')
def adminhome():
	return render_template('admin.html')

@admin.route('/kunde', methods=['GET','POST'])
@login_required
def kunde():
	pass

@admin.route('/baustelle', methods=['GET','POST'])
@login_required
def baustelle():
	pass

@admin.route('/kundenuebersicht', methods=['GET','POST'])
@login_required
def kundenuebersicht():
	pass

@admin.route('/mitarbeiter', methods=['GET','POST'])
@login_required
def mitarbeiter():
	pass

