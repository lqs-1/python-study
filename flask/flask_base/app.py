from flask import Flask, request, redirect, url_for, abort, make_response, jsonify, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



# 使用mysql还要安装pymysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lqs:lqs@localhost:3306/test'
# 关闭追踪的修改， 是sqlalchemy的事务通知系统， 会占用额外内存
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'  # 指定在数据库中的表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    # 定义外键，从底层考虑，真实的表名， 真是的字段进行关联
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    '''
        数据库：
            使用flask_sqlalchemy扩展管理数据库:
            from flask_sqlalchemy import SQLAlchemy
            扩展初始化：
                第一种
                db = SQLAlchemy()
                db.init_app(app)
                第二种
                db = SQLAlchemy(app)
        使用mysql还要安装pymysql
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lqs:lqs@localhost:3306/test'
        关闭追踪的修改， 是sqlalchemy的事务通知系统， 会占用额外内存
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        数据库模型：
            数据类型db.Column(db.类型,属性...)：
                Text：变长字符串，文本多的时候使用
                String：变长字符串，少量的时候使用，db.String(大小)
                Integer：普通整数
                Float：浮点数
                Date：python的datetime.date
                Time: python的datetime.time
                DataTime: python的datetime.datetime
                Boolean: 布尔值
                LargeBinary：二进制文件
            字段属性：
                primary_key:主键
                unique:是否唯一
                index:是否索引
                nullable:是否可以为空
                default:默认值
                
                
    
        清除数据库中所有的数据
        db.drop_all()
        创建表
        db.create_all()
    
        role = Role(name="stuff")
        用session记录需要执行的任务
        db.session.add(role)
        提交修改
        db.session.commit()
        如果发生错误就回滚事务
        db.session.rollback()
    
        user1 = User(name="李奇凇", role_id=1)
        user2 = User(name="罗成", role_id=2)
        user3 = User(name="罗峰", role_id=1)
        user4 = User(name="张三丰", role_id=2)
        user5 = User(name="李尚书", role_id=2)
        user6 = User(name="李光华", role_id=1)
    
        一次性添加多条
        db.session.add_all([user6,user5,user4,user3,user2,user1])
        db.session.commit()
        
        
    数据操作：
    对数据的操作可以使用模型类，也可以使用db.session
        查询：
        flask没查到就返回none，django没查到就报错
         role_list = Role.query.all()  /  role_list = db.session.query(Role).all() ：全查，返回列表
         Role.query.first()   /    db.session.query(Role).first() : 获取第一条
         Role.query.get(xx)    /    db.session.query(Role).get(xx): 获取一条，只能是id值
         
         filter和filter_by的区别：
            filter_by是要个匹配的，并且只能是and关系，也没有模糊查询，字段=xx
            filter是万能的，模型类.字段名==xx
         
         list = Role.query.filter_by(name="admin").first() : 获取name==admin的数据
         list = Role.query.filter_by(name="admin", id=2).first()  :  and关系 获取符合条件的数据
         
         list = User.query.filter(User.name=="李奇凇", User.id==6).first()   : 获取符合条件的数据，关系是and
         
         from sqlalchemy import or_ 
         list = User.query.filter(or_(User.name=="李奇凇",User.name.endswith("成")))  : 获取符合条件的数据，关系是or，结尾为成,startswith表示匹配开头
         
         
         user_list = User.query.filter(xxx).offset(x).limit(x).all():  offset表示跳过几条，limit表示显示几条
         
         user_list = User.query.filter(xx).order_by("-id").all() : 这种方法和django类似，但是不推荐
         user_list = User.query.filter(xx).order_by(User.id.desc()): 这种方式才是sqlalchemy通用的
         user_list = User.query.order_by(User.id.asc()): 这种方式才是sqlalchemy通用的,升序
         
         group_by:
            分组肯定会聚合
            from sqlalchemy import func
            db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id)  ： 凭借role_id来分组（在学习mysql的时候就说过，分组字段必须显示），在按照role_id计数
            分组只能用db.session.query()方式，query的参数就是分组之后要显示的字段，和聚合值
            普通查询中query的参数只能是 模型类名，因为分组查询之后并不是我们定义的模型，所以显示什么我们需要自己定义
            
    多表查询：
        建立外键关系：
            外键定义在多的一方：
                role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
            在一的一方定义关系：
                user = db.relationship('User', backref='role')
            有了外键和关系查询就方便多了
            多查一：
                多类模型.query.filter(xx).role
            一查多：
                一类模型.query.filter(xx).user
                
    更新：
        先查出来，在改
        role = Role.query.filter_by(name="admin").first()
        role.name = "xxx"
        db.session.add(role)
        db.session.commit()
        查询的同时更新
        Role.query.filter_by(name="admin").update({"name": "python","id": 3})
        db.session.commit()
        
    删除：
        先查出来，在删除
            role = Role.query.filter_by(name="admin").first()
            role.name = "xxx"
            db.session.delete(role)
            db.session.commit() 
    补充方法：
        默认显示：
            django默认显示用的是__str__方法，而在flask中我们使用的是__repr__方法，用法一样
        还可以补偿自定义的方法，比如转换字符串，转换成字典
        
         

    '''



class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    # 和外键相对应的属性，区别在于，外键是真是的一个字段，而这个不是
    # db.relationship是为了方便查询的，从模型的层面考虑， backref就是一个反推的属性
    # 设置好了backref之后，有相关有外键的表就可以靠  模型.backref的值进行查询这个表中的数据
    user = db.relationship('User', backref='role')

    def __repr__(self):
        return self.name











'''
    request对象：
        获取url：request.url
        获取请求参数：
            作用于get请求
                request.args.get('xx'): 用字典的方式获取值
            request.cookies: 获取随着请求一起带来的cookie
            作用于post请求
                request.get_json(): 获取前端传递被解析过的json数据，字典类型
                request.json(): 获取前端传递的json原数据
                
                request.form.get('name'): 获取表单中的数据， 没有文件的表单
                request.files.get('file'):  获取表单数据，有文件类型             
    response对象：
        response.make_response(字符串，页面，视图，json等等)
        response.mimetype = 'application/json'
        
'''




@app.route('/', methods=["GET"])
def hello_world():
    # 主动抛出异常
    # abort(404)

    # print(db)
    # 可以指定状态码
    # return 'Hello World!', 201

    # 重定向: 直接输入网址，或者配合url_for一起重定向到本地资源，url_for(目标视图名字)
    # return redirect('https://www.baidu.com')
    # return redirect(url_for('hello'))

    # 响应对象
    # response = make_response(hello)
    # response.mimetype = 'application/html'
    # response.headers.get("User-Agent")
    # return response

    # cookie
    # response.set_cookie['user'] = 12
    # response.set_cookie(key='name', value='lqs', max_age=60*3600)
    # response.delete_cookie(key='name')
    # request.cookies.get('name')
    # 返回json

    # session
    # session.get("xx")
    # session['xxx'] = 'xx'
    # session.pop('xxx')
    # if 'xx' in session:
    #     pass
    return jsonify({"name": 21})

@app.route('/index')
def hello():
    return '<h1>ok</h1>'






if __name__ == '__main__':
    # 获取路由表
    # print(app.url_map)
    app.run(debug=True)
