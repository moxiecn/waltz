import logging
import os

from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
# from flask_uploads import UploadSet, IMAGES
from flask_wtf import CSRFProtect

from config import config

configName = os.getenv('FLASK_CONFIG') or 'default'

# # 實例化一個全局logger對象
xlogger = logging.getLogger(config[configName].LOG_NAME)

# Flask_SQLALChemy组件初始化
db = SQLAlchemy()

# 實例化一個flask-session對象
session = Session()

# # 實例化一些插件的全局对象
loginmanager = LoginManager()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()

# # 實例化一个CSRF保护的全局对象
csrf = CSRFProtect()  # 安全KEY使用flask默认的SECRET_KEY

# Flask_uploads组件初始化,创建一个flask_uploads集合,供manage.py中的处理函数引用.
# 之所以放到这里初始化,是因为这些上传的文件被我视为数据库的一部分,当然也可以在别的地址初始化它
# 通过UploadSet函数创建一个Set,允许上传哪些类型的文件
#uploadSetPhotos = UploadSet('photos', IMAGES)

pass
