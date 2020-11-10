import os
#import sys
import time
import logging

#from log import alog

# 重新导入sys,之后强制默认sys的字符集编码为utf-8,为了防止操作系统的默认编码不是utf-8
# 这是python3中的写法
# import importlib
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')

basedir = os.path.abspath(os.path.dirname(__file__))

#各类基础组件的配置参数集，项目运行后必须先加载这里
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'  # 为CSRF保护创建SECRET_KEY设置

    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = '119161229@qq.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    SSL_DISABLE = False
    DEBUG = False

    LOGINMANAGER_LOGIN_VIEW = 'bp_base.login'  # flask-login组件的默认登录页面,flask-login组件的参数，当组件验证授权不成功时跳转到这里指定的登录页面

    # SQLALCHEMY参数设置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 开启_自动提交
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 开启_跟踪对象修改并发出信号
    SQLALCHEMY_RECORD_QUERIES = True  # 开启_查询记录
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 15

    # FLASK文件上傳组件
    UPLOAD_FOLDER = '/tmp/www/uploading/'  # 服務端將文件永久保存的路徑
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # FLASK上傳每個文件最大尺寸(字節)
    UPLOADED_PHOTOS_DEST = '/tmp/www/uploading/photos'  # 服務端將图片文件永久保存的路徑
    MAX_PHOTO_LENGTH = 16 * 1024 * 1024  # FLASK上傳每個图片文件最大尺寸(字節)

    # falsk.logging组件参数集
    LOG_LEVEL = logging.ERROR  # 日誌記錄的最低等級
    LOG_MAX_SIZE = 100 * 1024 * 1024  # 每个日志文件的最大尺寸(字节_100MB)
    LOG_BACKUPCOUNT = 100  # 保存的日志文件个数上限
    # 定義日誌內容的格式
    LOG_FORMATTER1 = "%(asctime)s - [%(lineno)d.%(levelname)s.%(name)s] - %(filename)s/%(funcName)s - %(message)s"
    # 定義日誌內容的格式
    LOG_FORMATTER2 = "%(asctime)s - [%(lineno)d.%(levelno)s.%(levelname)s.%(name)s] - %(filename)s.%(funcName)s - %(message)s"
    # 定義日誌內容的格式
    LOG_FORMATTER3 = '%(levelname)s %(filename)s:%(lineno)d %(message)s'
    LOG_STORAGE_PATH = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "log/log")  # 日志文件根路徑
    if not os.path.exists(LOG_STORAGE_PATH):  # 创建日志目录
        os.makedirs(LOG_STORAGE_PATH)
    # LOG_NAME = 'flasker' + os.path.split(os.path.splitext(sys.argv[0])[0])[-1]
    LOG_NAME = 'teset02'
    LOGFILE_NAME = LOG_NAME + "_" + \
        time.strftime("%z_%Y%m%d.log", time.localtime())

    # flask-session組件參數集
    # 是否为cookie设置签名来保护数据不被更改，默认是False；如果设置True, 那么必须设置flask的secret_key参数；
    SESSION_USE_SIGNER = True
    # 是否使用永久会话，默认True，但是如果设置了PERMANENT_SESSION_LIFETIME，则这个即使设置为true也失效；
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = 60  # 會話有效期(秒)
    # SESSION_KEY_PREFIX = 'session:'  # session存储时的键的前缀
    SESSION_REFRESH_EACH_REQUEST = True  # 每次请求都刷新session
    # SESSION_TYPE = None  # 采用flask默认的保存在cookie中；
    SESSION_CLEANUP_INTERVAL = 60 * 60 * 24  # 会话定期清理时间间隔,由flask-kvsession组件处理

    SESSION_TYPE = 'filesystem'  # 保存在文件時的參數集
    SESSION_FILE_THRESHOLD = 500  # 存储session的个数如果大于这个值时，就要开始进行删除了
    SESSION_FILE_MODE = 384  # 文件权限类型
    SESSION_FILE_DIR = os.path.join(basedir, 'session')  # Session保存的完全路徑

    # SESSION_TYPE = 'redis'  # 保存在redis中
    # SESSION_TYPE = 'memcached'  # 保存在memcache
    # SESSION_TYPE = 'mongodb'  # 保存在MongoDB
    # SESSION_TYPE = 'sqlalchemy'  # 保存在关系型数据库

    #暂时没有作任何初始化处理
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # falsk_SQLALCHEMY组件参数集
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'python'
    USERNAME = 'python'
    PASSWORD = '12345678'

    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                            password=PASSWORD,
                                                                                            host=HOST, port=PORT,
                                                                                            db=DATABASE)

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or DB_URI
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # falsk.logging组件参数集
    LOG_LEVEL = logging.DEBUG

    # flask-session組件參數集
    SESSION_PERMANENT = False  # 是否使用永久会话，默认True，但是如果设置了PERMANENT_SESSION_LIFETIME，则这个失效；

    # SESSION_TYPE = 'filesystem'  # 保存在文件



class TestingConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

#各类config配置的元组
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# ##################################
# #Flask-SQLAlchemy的数据库连接参数
# ##################################
# HOST = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'python'
# USERNAME = 'python'
# PASSWORD = '12345678'
# #DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)
# DB_URI = "mysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)
#
# #[必须设置]设置数据库连接URI,其格式为：mysql://username:password@server/db？编码.注意默认使用mysqldb连接数据库，要使用pymysql就需要用mysql+pymysql的格式；
# SQLALCHEMY_DATABASE_URI = DB_URI
#
# ##################################
# #Flask-SQLAlchemy的系统级参数配置
# ##################################
#
# #一个映射绑定 (bind) 键到 SQLAlchemy 连接 URIs 的字典。他可以用来连接多个数据库。详情参阅：http://www.pythondoc.com/flask-sqlalchemy/binds.html#binds
# #SQLALCHEMY_BINDS = {
# #    'users':        'mysqldb://localhost/users',
# #    'appmeta':      'sqlite:////path/to/appmeta.db'
# #}
#
# #[常用设置]设置是否在每次连接结束后自动提交数据库中的变动。
# SQLALCHEMY_COMMIT_ON_TEARDOWN = True
#
# #数据库池的大小，默认值为5。
# SQLALCHEMY_POOL_SIZE = 10
#
# #指定数据库连接池的超时时间。默认是 10。
# SQLALCHEMY_POOL_TIMEOUT = 10
#
# #[常用设置]自动回收连接的秒数。
# # 这对MySQL是必须的，默认情况下MySQL会自动移除闲置8小时或者以上的连接,Flask-SQLAlchemy会自动地设置这个值为 2 小时。
# # 也就是说如果连接池中有连接2个小时被闲置，那么其会被断开和抛弃；
# SQLALCHEMY_POOL_RECYCLE=1200
#
# #[不用设置]可以用于显式地禁用或者启用查询记录。查询记录 在调试或者测试模式下自动启用。一般不用明显地设置。
# #SQLALCHEMY_RECORD_QUERIES
#
# #[不用设置]可以用于显式地禁用支持原生的unicode。一般不用明显地设置。
# #SQLALCHEMY_NATIVE_UNICODE
#
# #[不用用设置]可以用于显式地禁用或者启用查询记录。查询记录 在调试或者测试模式下自动启用。一般不用明显地设置。
# #SQLALCHEMY_MAX_OVERFLOW
#
#
# #[调用时打开]如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# #[调用时打开]如果设置成 True，SQLAlchemy 将会记录所有发到标准输出(stderr)的语句，这对调试很有帮助;默认为false；
# SQLALCHEMY_ECHO = True
#
# ##################################
# #Flask-SQLAlchemy常用字段类型
# ##################################
# # 类型名                       python类型           说明
# # Integer                     int                  普通整数，一般是32位
# # SmallInteger                int                  取值范围小的整数，一般是16位
# # BigInteger                  int或long            不限制精度的整数
# # Float                       float                浮点数
# # Numeric                     decimal.Decimal      普通整数，一般是32位
# # String                      str                  变长字符串
# # Text                                str                  变长字符串，对较长或不限长度的字符串做了优化
# # Unicode                     unicode              变长Unicode字符串
# # UnicodeText                 unicode              变长Unicode字符串，对较长或不限长度的字符串做了优化
# # Boolean                     bool                 布尔值
# # Date                        datetime.date        时间
# # Time                        datetime.datetime    日期和时间
# # LargeBinary                 str                  二进制文件
# # Enum                        enum                 枚举类型
# ##################################
# #Flask-SQLAlchemy常用列定义时的修饰选项
# ##################################
# # primary_key         如果为True，代表表的主键
# # unique              如果为True，代表这列不允许出现重复的值
# # index               如果为True，为这列创建索引，提高查询效率
# # nullable            如果为True，允许有空值，如果为False，不允许有空值
# # default             为这列定义默认值,如default=1
# ##################################
# #Flask-SQLAlchemy常用的表间关系修饰选项
# ##################################
# # backref             在关系的另一模型中添加反向引用,用于找到父表
# # primary join        明确指定两个模型之间使用的联结条件
# # uselist             如果为False，不使用列表，而使用标量值
# # order_by            指定关系中记录的排序方式
# # secondary           指定多对多中记录的排序方式
# # secondary join      在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件
