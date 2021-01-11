from flask import Blueprint, render_template	
from application import db

admin = Blueprint('admin',__name__, template_folder='templates')

@admin.route('/admin', methods=['GET','POST'])
def adminhome():
	return render_template('admin.html')

@admin.route('/kunde', methods=['GET','POST'])
def kunde():
	pass

@admin.route('/baustelle', methods=['GET','POST'])
def baustelle():
	pass

@admin.route('/kundenuebersicht', methods=['GET','POST'])
def kundenuebersicht():
	pass

@admin.route('/mitarbeiter', methods=['GET','POST'])
def mitarbeiter():
	pass

