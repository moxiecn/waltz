from flask import render_template
from flask_login import login_required

from ..blueprint import bp_base
from ..global_.exts import xlogger, db
from ..models.User import User


@bp_base.route('/')
@login_required
def index():
    xlogger.info("进入主页bp_base./")
    return render_template('index.html')


@bp_base.route("/doit")
def dofunc():
    pass
    user = User.query.filter_by(ID='0').first()
    return str(db.engine) + "..." + user.LOGINNAME


# @csrf.exempt
@bp_base.route('/base/north', methods=['POST'])
@login_required
def north():
    xlogger.info("执行NORTH")
    return render_template('layout/north.html')


@bp_base.route('/base/west', methods=['POST'])
@login_required
def west():
    return render_template('layout/west.html')


@bp_base.route('/base/south', methods=['POST'])
@login_required
def south():
    return render_template('layout/south.html')


@bp_base.route('/style/icons.jsp')
def icons():
    return render_template('icons/icons.html')
