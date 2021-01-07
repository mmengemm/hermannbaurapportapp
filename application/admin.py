from flask import Blueprint, render_template	
from . import db

main = Blueprint('main',__name__)

@main.route('/admin', methods=['GET','POST'])
def admin():
	return render_template('admin.html')

