from flask import Blueprint

# blueprint = Blueprint('blueprint', __name__, url_prefix='/blueprint')
# 创建一个名字为'blueprint'的蓝图,用于项目基础蓝图
# 第一个参数是蓝图的名字,
# 第二个参数是告诉蓝图它是在哪里创建的,本例是在app.base下,__name__=app.blueprint,当前文件所在目录,
# 第三个参数本例没有声明,url_prefix='/blueprint',url_prefix 会添加到所有与该蓝图关联的 URL 前面.
bp_base = Blueprint('bp_base', __name__)
# 創建 用於測試的 登錄蓝图,
#bp_login = Blueprint('bp_login', __name__, url_prefix='/bp_login')
# 创建图片上传蓝图,
#bp_uploadPics = Blueprint('bp_upp', __name__, url_prefix='/bp_uploading/pics')

# 从routes目录下导入全项目全部的路由定义
from ..routes import *
#from ..routes.login import *
