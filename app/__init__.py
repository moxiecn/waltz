import logging
import os
import sys

from flask import Flask
from flask_uploads import configure_uploads, patch_request_class

from app.global_.exts import db, session, xlogger, bootstrap, mail, moment, loginmanager, csrf
from app.models import User
from config import config, basedir


# 统一入口创建app函数,成功后返回app对象.实例化在manage.py中执行.
def create_app(configName):
    # 如果不满断言成立条件则抛出assererror异常.
    assert ('darwin' in sys.platform), "该代码只能在 MACOSX 下执行" + sys.platform

    # 實例化一個falsk對象
    app1 = Flask(__name__, instance_relative_config=True,
                 template_folder='../templates', static_folder="../static")
    # , static_folder = "",    static_url_path = ""
    # xlogger.info("Flask已实例化." + __name__)
    xlogger.info('Flask已实例化.')
    xlogger.info("Basedir of the project is: " + basedir)
    xlogger.info("The dbsn is: " + config[configName].SQLALCHEMY_DATABASE_URI)

    # 配置app1实例,從字典config中查找相應的Config
    app1.config.from_object(config[configName])
    # app1实例配置参数加载之后，调用自定义的app初始化,这里暂时是预留的空方法
    config[configName].init_app(app1)
    app1.secret_key = app1.config['SECRET_KEY']
    xlogger.info("Flask实例app1的配置已加载.-[" + configName +
                 "]-SECRET_KEY=[" + app1.config['SECRET_KEY'] + "]")

    # 初始化flask-sqlalchemy组件.
    # 这个函数其读取app的配置参数，将和数据库相关的配置加载到SQLAlchemy对象中,将新的flask实例对象app1和刚实例化好的db对象绑定
    db.init_app(app1)
    xlogger.info("Flask实例app1已经和炼金术对象db绑定.")

    # 初始化csrf
    csrf.init_app(app1)
    xlogger.info("Flask实例app1已经設置CSRF保護.")

    # 初始化flask-session,本组件要用到werkzug.contrib.
    # werkzeug1.0中被删除,要安装0.16.0版本的werkzeug
    session.init_app(app=app1)  # 將session實例綁定到app1實例,對象實例化在global_.exts中
    xlogger.info("Flask实例app1已经設置自定義session.")

    # 初始化flask_uploads上传组件.
    # 类似大多数flask扩展组件的初始化方式,使用configure_uploads函数将Flask_uploads组件绑定至app,并指定上面创建的photos set,
    # 成功之后就可用set名在app中操作上传的文件,如保存文件\获得文件url\获取文件绝对地址等.类似于db对象集合了对数据库操作一样.
    #configure_uploads(app1, uploadSetPhotos)
    # set maximum file size, default is 16MB
    patch_request_class(app1, app1.config['MAX_PHOTO_LENGTH'])
    xlogger.info("Flask实例app1已经設置自定義上傳組件.")

    # 初始化一些全局插件
    bootstrap.init_app(app1)
    mail.init_app(app1)
    moment.init_app(app1)
    loginmanager.session_protection = 'strong'
    # 对应的登录页面路由定义在index.py中的/login
    loginmanager.login_view = app1.config['LOGINMANAGER_LOGIN_VIEW']
    loginmanager.init_app(app1)

    # 绑定蓝图
    from app.blueprint import bp_base as bp_base
    #from app.blueprint import bp_login
    #from app.blueprint import bp_uploadPics
    app1.register_blueprint(bp_base)
    #app1.register_blueprint(bp_login)
    #app1.register_blueprint(bp_uploadPics)
    xlogger.error("Flask实例app1已经綁定藍圖.")

    return app1


# 原生全局日志组件的配置和初始化,基于app.logging.getLogger()
def setup_rawlog(config_name):
    # 實例化一個全局logger對象
    #  xlogger = logging.getLogger(config[config_name].LOG_NAME)
    # xlogger對象在app.global_.exts中被初始化,導入後可以直接使用

    # 设置日志的记录等级
    xlogger.setLevel(config[config_name].LOG_LEVEL)  # 设置日志级别
    print("配置日誌組件-級別運行在[" + str(config[config_name].LOG_LEVEL) + "]")

    # 定義一個通用的日誌格式
    log_formatter = logging.Formatter(config[config_name].LOG_FORMATTER1)
    print("配置日誌組件-被格式化成[" + config[config_name].LOG_FORMATTER1 + "]")

    handler_list = list()  # 聲明一個處理器list對象
    # 構造一個文件型日誌處理器
    from logging.handlers import RotatingFileHandler
    logfilename = os.path.abspath(
        os.path.join(config[config_name].LOG_STORAGE_PATH, config[config_name].LOGFILE_NAME))
    loghandler_file = RotatingFileHandler(
        filename=logfilename,
        maxBytes=config[config_name].LOG_MAX_SIZE,
        backupCount=config[config_name].LOG_BACKUPCOUNT,
        encoding="utf-8")
    loghandler_file.setLevel(config[config_name].LOG_LEVEL)
    # loghandler_file.addFilter(LogFilterInfo())
    handler_list.append(loghandler_file)  # list中放一個文件型日誌處理器以utf8編碼
    print("配置日誌組件-日誌文件放在[" + logfilename + "]")
    # 構造一個控制臺型日誌處理器
    handler_list.append(logging.StreamHandler())
    print("配置日誌組件-日誌向控制臺輸出.")

    # 將handler綁定到全局的日志工具对象上（flask app使用的）
    for handler in handler_list:  # 將以上放在list中的處理器統一格式化
        handler.setFormatter(log_formatter)
        xlogger.addHandler(handler)


# 暫不啓用,定義一個日誌過濾器_info型的
class LogFilterInfo(logging.Filter):
    def filter(self, record):
        """only use INFO
        筛选, 只需要 INFO 级别的log
        :param record:
        :return:
        """
        if logging.INFO <= record.levelno < logging.ERROR:
            # 已经是INFO级别了
            # 然后利用父类, 返回 1
            return super().filter(record)
        else:
            return 0
