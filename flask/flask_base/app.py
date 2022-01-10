from flask import Flask, request, redirect, url_for, abort, make_response, jsonify

app = Flask(__name__)


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
    # 可以指定状态码
    # return 'Hello World!', 201

    # 重定向: 直接输入网址，或者配合url_for一起重定向到本地资源，url_for(目标视图名字)
    # return redirect('https://www.baidu.com')
    # return redirect(url_for('hello'))

    # 响应对象
    response = make_response(hello)
    # response.mimetype = 'application/html'
    # response.headers.get("User-Agent")
    # return response

    # cookie
    # response.set_cookie['user'] = 12
    # response.set_cookie(key='name', value='lqs', max_age=60*3600)
    # response.delete_cookie(key='name')
    # request.cookies.get('name')
    # 返回json
    return jsonify({"name": 21})


@app.route('/index')
def hello():
    return '<h1>ok</h1>'
if __name__ == '__main__':
    # 获取路由表
    print(app.url_map)
    app.run(debug=True)
