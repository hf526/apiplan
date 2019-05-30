from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.app import db


class Base:
    create_time = db.Column(db.DateTime, default=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), comment="更新时间")

    def add_update(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    def delete_data(self):
        try:
            self.status = 1
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(e)
            return False


class User(Base, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(128), comment="用户昵称", default="未填写昵称用户")
    username = db.Column(db.String(128), unique=True, comment="用户名")
    pwd_hash = db.Column(db.String(512), comment="密码")
    status = db.Column(db.Integer, comment="状态,0正常 1删除", default=0)
    create_time = db.Column(db.DateTime, default=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), comment="更新时间")

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.hspassword = password

    # 读
    @property
    def hspassword(self):
        return ''

    # 写
    @hspassword.setter
    def hspassword(self, password):
        self.pwd_hash = generate_password_hash(password)

    # 对比
    def check_pwd(self, pwssword):
        return check_password_hash(self.pwd_hash, pwssword)

    def __repr__(self):
        return '<Project %r>' % self.__tablename__


class Role(Base, db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    username = db.Column(db.String(128), unique=True, comment="用户名")
    role = db.Column(db.Integer, comment="用户角色")

    def __repr__(self):
        return '<Role %r>' % self.__tablename__


class Project(Base, db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(80), unique=True, comment="项目名称")
    comment = db.Column(db.String(80), comment="项目描述")
    status = db.Column(db.Integer, comment="状态")

    def __repr__(self):
        return '<Project %r>' % self.__tablename__


class Case(Base, db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(80), comment="用例名称")
    comment = db.Column(db.String(512), comment="用例描述")
    expect = db.Column(db.String(512), comment="期望响应结果")
    response = db.Column(db.String(512), comment="实际响应结果")
    status = db.Column(db.Integer, comment="状态")

    def __repr__(self):
        return '<Case %r>' % self.__tablename__


class Api(Base, db.Model):
    __tablename__ = 'api'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    path = db.Column(db.String(80), comment="接口地址")
    header = db.Column(db.String(80), comment="请求头")
    method = db.Column(db.String(128), comment="请求方式")
    data = db.Column(db.String(512), comment="接口参数")
    status = db.Column(db.Integer, comment="状态")

    def __repr__(self):
        return '<Api %r>' % self.__tablename__


class WebConfig(Base, db.Model):
    __tablename__ = 'webconfig'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(80), comment="配置名称")
    url = db.Column(db.String(80), comment="环境地址")
    header = db.Column(db.String(80), comment="公共请求头")
    status = db.Column(db.Integer, comment="状态")

    def __repr__(self):
        return '<Api %r>' % self.__tablename__


class Logs(Base, db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    operation = db.Column(db.String(80), comment="操作描述")
    operautor = db.Column(db.String(80), comment="操作人")
    client = db.Column(db.Integer, comment="最后操作的客户端")

    def __repr__(self):
        return '<Api %r>' % self.__tablename__


class Variable(Base, db.Model):
    __tablename__ = 'variable'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    variable_name = db.Column(db.String(80), comment="变量名称")
    script = db.Column(db.String(80), comment="脚本")

    def __repr__(self):
        return '<Api %r>' % self.__tablename__
