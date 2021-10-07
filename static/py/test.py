# 필요한 모듈 import 
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
 
main = Blueprint('py', __name__, url_prefix='/') # url_prefix : '/'로 url을 붙여라
 
@main.route('/py', methods=['GET'])
def index():
      return render_template('/py/index.html')