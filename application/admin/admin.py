from flask import Blueprint, render_template	
from application import db

admin = Blueprint('admin',__name__)

@admin.route('/admin', methods=['GET','POST'])
def admin():
	return render_template('admin.html')

