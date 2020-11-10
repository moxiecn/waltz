# -*- coding: utf-8 -*-

from flask import render_template, g, request
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from flask_wtf.csrf import CSRFError

from app import create_app, setup_rawlog
from app.blueprint import bp_base
from app.global_.exts import configName, xlogger
from app.models.User import User

# 設置原生日誌組件
setup_rawlog(configName)

# 調用app.factory中的create_app,獲得app根對象
app = create_app(configName)

# 初始實例化一個基於Flask-script的命令管理器manager
# 基礎的用法參見:https://blog.csdn.net/twc829/article/details/52154214
manager = Manager(app)

# Flask-Migrate是一个扩展，使用 Alembic 处理 Flask 程序的 SQLAlchemy
# 数据库迁移。详情参见:https://blog.csdn.net/Noizfun/article/details/81182691
from app.global_.exts import db

migrate = Migrate(app, db)


@app.errorhandler(CSRFError)
def csrf_error(reason):
    # return render_template('errors/400_csrfError.html'), 400
    return render_template('errors/400_csrfError.html', reason=reason), 400


# @app.before_request
# def check_csrf():
#     # request.headers.add("X-CSRFToken",getCookie("csrf_token"))
#     xlogger.info("请求之前:"+request.method)
#     xlogger.info("请求之前:"+request.url)
#     xlogger.info("请求之前:"+str(request.data))
#     xlogger.info("请求之前:"+str(request.path))
#     xlogger.info("请求之前:"+str(request.headers))
#     xlogger.info("请求之前:"+str(request.form))
#     # if not is_oauth(request):
#     #     csrf.protect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

# # init Flask-KVSession
# engine = create_engine('mysql+pymysql://user:password@localhost/kvsession_db')
# metadata = MetaData(bind=engine)
# store = SQLAlchemyStore(engine, metadata, 'kvsession_table')
# metadata.create_all()
# kvsession_extension = KVSessionExtension(store, app)
#
# # perdiocally cleanup expired sessions
# import time
# # do cleanup per day. You may store this value in app.config
# deadline = None
# @app.after_request
# def cleanup_expired_sessions():
#     global SESSION_CLEANUP_INTERVAL, deadline
#     if deadline is None:
#         kvsession_extension.cleanup_sessions(app)
#         deadline = time.time() = SESSION_CLEANUP_INTERVAL
#     else:
#         if time.time() >= deadline:
#             # time to do cleanup
#             kvsession_extension.cleanup(app)
#             # update deadline
#             deadline = time.time() + SESSION_CLEANUP_INTERVAL


# ?with语句用于上下文处理,python的上下文管理机制,详情参见:https://www.cnblogs.com/wongbingming/p/10519553.html
# 功能上类似于sql中的with语句,基本语法是:
# with expression as var:
#   problock
with app.app_context():
    g.contextPath = ''
    # db.drop_all()
    # db.create_all()


# shell命令的上下文处理函数,本函数中将本app,db和本应用中用到的全部db模组导入python
# shell环境中,这样可以在新的shell环境中直接操作使用本app中的各类已构造对象.
def make_shell_context():
    return dict(app=app, db=db, User=User)
    # Role=Role, Resource=Resource,
    #             ResourceType=ResourceType, Organization=Organization)


# 增加shell命令,shell上下文绑定到make_shell_context函数.传入函数对象即可,不能执行
manager.add_command("shell", Shell(make_context=make_shell_context))
# 增加db命令,
manager.add_command('db', MigrateCommand)


# 以@manager.command注释将myprint函数声明为一个新的自定义命令
@manager.command
def myprint():
    xlogger.info("Hello world")
    print('hello world')


if __name__ == '__main__':
    xlogger.info("__main__准备")
    xlogger.info(app.url_map)
    # app.run()  # 直接運行flask框架下的app
    manager.run()  # 以命令方式運行,如果要運行flask框架下的app,執行這個命令: python3.6 manage.py runserver
    xlogger.info("__main__完成")

# @app.route('/jinja/')
# @app.route('/jinja/<name_>')
# def jinja01(name_=None):
#     return render_template('hello.html', name=name_)


# # 允許上傳文件類型
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'dmg'}
#
#
# # 檢查FLASK上傳文件的擴展名是否合法
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
#
# # 设置静态文件缓存过期时间
# app.send_file_max_age_default = timedelta(seconds=1)
#
#
# @app.route('/uploadfile/', methods=['GET', 'POST'])
# def upload_file():
#     xlogger.info(app.config['UPLOAD_FOLDER'])
#     if request.method == 'POST':
#         # check if the post request has the file part,檢查收到的POST請求中files對象是否包含file
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # 如果用戶端沒有選擇文件,瀏覽器也會提交一個沒有文件名的空對象
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             xlogger.info(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file', filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file multiple>
#       <input type=submit value=Upload>
#     </form>
#     '''
#
#
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)


# class UploadForm(FlaskForm):
#     photo = FileField(validators=[
#         FileAllowed(uploadSetPhotos, u'只能上传图片！'),
#         FileRequired(u'文件未选择！')])
#     submit = SubmitField(u'上传')
#
#
# @app.route('/uploadphoto', methods=['GET', 'POST'])
# @app.route('/uploadphoto/', methods=['GET', 'POST'])
# def upload_file():
#     form = UploadForm()
#     if form.validate_on_submit():
#         filename = uploadSetPhotos.save(form.photo.data)
#         file_url = uploadSetPhotos.url(filename)
#         xlogger.info("FILENAME=" + filename)
#         xlogger.info("FILEURL=" + file_url)
#     else:
#         file_url = None
#     return render_template('uploadphoto.html', form=form, file_url=file_url)
#
#
# class MUploadForm(FlaskForm):
#     photo = FileField(validators=[FileAllowed(uploadSetPhotos, u'Image Only!'), FileRequired(u'Choose a file!')])
#     submit = SubmitField(u'Upload')
#
#
