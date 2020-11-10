import hashlib
import uuid
from datetime import datetime

from flask import jsonify, session
from flask import render_template, request
from flask_login import login_user, logout_user

from ..blueprint import bp_base
from ..models.User import User
#from ..models.Organization import Organization
#from ..models.Role import Role
from ..global_.exts import xlogger, db


@bp_base.route('/login', methods=['GET'])
def login():
    xlogger.debug("处理login")
    return render_template('login.html')


@bp_base.route('/securityJsp/base/SyuserForm.jsp', methods=['GET'])
def form_user():
    return render_template('user/form.html', id=request.args.get('id', ''))


@bp_base.route('/securityJsp/base/SyuserOrganizationGrant.jsp', methods=['GET'])
def grant_user_organization_page():
    return render_template('user/grant_organization.html', id=request.args.get('id', ''))


@bp_base.route('/securityJsp/base/SyuserRoleGrant.jsp', methods=['GET'])
def grant_user_role_page():
    return render_template('user/grant_role.html', id=request.args.get('id', ''))


@bp_base.route('/base/syuser!grantOrganization.action', methods=['POST'])
def grant_user_organization():
    id = request.form.get('id')
    ids = request.form.get('ids')

    user = User.query.get(id)

    if not ids:
        user.organizations = []
    else:
        idList = ids.split(',')
        user.organizations = [Organization.query.get(rid) for rid in idList]

    db.session.add(user)

    return jsonify({'success': True})


@bp_base.route('/base/syuser!grantRole.action', methods=['POST'])
def grant_user_role():
    id = request.form.get('id')
    ids = request.form.get('ids')

    user = User.query.get(id)

    if not ids:
        user.roles = []
    else:
        idList = ids.split(',')
        user.roles = [Role.query.get(rid) for rid in idList]

    db.session.add(user)

    return jsonify({'success': True})


# 登录验证处理动作.响应/login.html中的表单(form_login)的post提交
@bp_base.route('/base/syuser!doNotNeedSessionAndSecurity_login.action', methods=['POST'])
def do_login():
    # 检查用户名是否存在
    user = User.query.filter_by(
        LOGINNAME=request.form['data.loginname']).first()
    if user is not None:
        md = hashlib.md5()
        # 提交的密码MD5加密
        md.update(request.form['data.pwd'].encode('utf-8'))
        # MD5加密后的内容同数据库密码比较
        if md.hexdigest() == user.PWD:
            # 调用flask-login框架的登录函数,将当前user对象的相关信息放入session中
            login_user(user)
            session['currUserId'] = user.ID
            session['currUserName'] = user.NAME
            session['currUserLoginName'] = user.LOGINNAME
            xlogger.debug("登录成功." + user.ID + "-" +
                          user.NAME + "-" + user.LOGINNAME)
            return jsonify({'success': True, 'msg': '登录成功!'})
    return jsonify({'success': False, 'msg': '登录不成功!'})


# 解锁登出验证处理动作.响应/index.html中的unlockDialog对象中的post提交
@bp_base.route('/base/syuser!doNotNeedSessionAndSecurity_lock.action', methods=['POST'])
def do_unlock():
    user_id = session['currUserId']
    user_loginname = session['currUserLoginName']
    logout_user()
    session.pop("currUserId")
    session.pop("currUserName")
    session.pop("currUserLoginName")

    xlogger.info('锁定成功.' + user_id + "-" + user_loginname)
    del user_id, user_loginname
    return jsonify({'success': True, 'msg': '已经锁定!'})


# 登出验证处理动作.响应/login.html中的表单(form_login)的post提交
@bp_base.route('/base/syuser!doNotNeedSessionAndSecurity_logout.action', methods=['POST'])
def do_logout():
    user_id = session['currUserId']
    user_loginname = session['currUserLoginName']
    logout_user()
    session.clear()
    xlogger.info('登退成功.' + user_id + "-" + user_loginname)
    del user_id, user_loginname
    return jsonify({'success': True, 'msg': '已经登退!'})


# 修改当前登录者密码动作
# @csrf.exempt
@bp_base.route('/base/syuser!doNotNeedSecurity_updateCurrentPwd.action', methods=['POST'])
def do_updatePwdForCurrentUser():
    user = User.query.filter_by(ID=str(session['currUserId'])).first()
    newpwd = request.form['data.pwd']
    xlogger.info("[修改密码]-当前登录用户" +
                 str(session['currUserLoginName']) + "..." + newpwd)
    if user is not None:
        md = hashlib.md5()
        # 提交的密码MD5加密
        md.update(newpwd.encode('utf-8'))
        user.PWD = md.hexdigest()
        db.session.add(user)
        db.session.commit()
        return jsonify({'success': True, 'msg': '当前登录者密码修改成功!'})

    del user, newpwd
    return jsonify({'success': False, 'msg': '修改密码不成功!'})
    # return jsonify({'success': False, 'msg': '登录不成功!'})


@bp_base.route('/securityJsp/base/Syuser.jsp', methods=['GET'])
def index_user():
    return render_template('user/index.html')


@bp_base.route('/base/syuser!grid.action', methods=['POST'])
def user_grid():
    page = request.form.get('page', 1, type=int)
    rows = request.form.get('rows', 10, type=int)
    pagination = User.query.paginate(
        page, per_page=rows, error_out=False)
    users = pagination.items

    return jsonify([user.to_json() for user in users])


@bp_base.route('/base/syuser!getById.action', methods=['POST'])
def syuser_getById():
    user = User.query.get(request.form.get('id'))

    if user:
        return jsonify(user.to_json())
    else:
        return jsonify({'success': False, 'msg': 'error'})


@bp_base.route("/securityJsp/userInfo.jsp", methods=['GET'])
def syuser_curruser_info():
    id = str(session['currUserId'])
    user = User.query.get(id)
    return render_template('user/show_curuser_info.html', current_user=user)


@bp_base.route('/base/syuser!update.action', methods=['POST'])
def syuser_update():
    id = request.form.get('data.id')
    loginname = request.form.get('data.loginname')

    if User.query.filter(User.LOGINNAME == loginname).filter(User.ID != id).first():
        return jsonify({'success': False, 'msg': '更新用户失败，用户名已存在！'})

    user = User.query.get(id)

    user.UPDATEDATETIME = datetime.now()
    user.LOGINNAME = request.form.get('data.loginname')
    user.NAME = request.form.get('data.name')
    user.SEX = request.form.get('data.sex')
    user.PHOTO = request.form.get('data.photo')

    db.session.add(user)

    return jsonify({'success': True, 'msg': '更新成功！'})


@bp_base.route('/base/syuser!save.action', methods=['POST'])
def syuser_save():
    if User.query.filter_by(LOGINNAME=request.form.get('data.loginname')).first():
        return jsonify({'success': False, 'msg': '新建用户失败，用户名已存在！'})

    user = User()

    user.ID = uuid.uuid4()

    md = hashlib.md5()
    md.update('123456')
    user.PWD = md.hexdigest()

    user.NAME = request.form.get('data.name')
    user.LOGINNAME = request.form.get('data.loginname')
    user.SEX = request.form.get('data.sex')
    user.PHOTO = request.form.get('data.photo')

    # add current use to new user
    # current_user.roles.append(user)

    db.session.add(user)

    return jsonify({'success': True, 'msg': '新建用户成功！默认密码：123456'})


@bp_base.route('/base/syuser!delete.action', methods=['POST'])
def syuser_delete():
    user = User.query.get(request.form.get('id'))
    if user:
        db.session.delete(user)

    return jsonify({'success': True})
