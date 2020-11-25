from flask import Flask, url_for, render_template
from flask_restful import Api, Resource, reqparse, inputs
from flask_sqlalchemy import SQLAlchemy
import config

'''
（输入） Flask_restful01 有一个验证、类似于wtf的验证   （输入验证）
 通过 postman 进行输入
'''
app = Flask(__name__)
api = Api(app)
app.config.from_object(config)
db = SQLAlchemy(app)


# class Aa(db.Model):
#     __tablename__ = "aa"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64))
#     password = db.Column(db.String(64))


# 这是一个接受ajax数据的api
class Send_ajax(Resource):
    '''
    只定义一个post请求
    '''

    def post(self):
        # 获取解析对象
        parser = reqparse.RequestParser()

        parser.add_argument("password",  required=True)
        parser.add_argument("username",  required=True)

        # 拿到这个传来的参数
        args = parser.parse_args()

        # 打印ajax传递来的参数
        print("获取全部传来的值:", args)

        # 获取username的字段
        print("打印前端传来的值：", args.get("username"))
        print("打印前端传来的值：", args.get("password"))
        # aa = Aa(username=args.get("username"), password=args.get("password"))
        # db.session.add(aa)
        # db.session.commit()

        return {"password": args.get("password")}


# 方式一、在Postman里面输入：http://127.0.0.1:8888/login/?username=哇咔咔 会传递信息 哇咔咔 给username
# 方式二、通过jquery的方式、给后端进行传参、
api.add_resource(Send_ajax, "/index/")


@app.route('/')
def index():
    print("主页")
    return render_template("index.html")


# @app.route('/long/')
# def long():
#     print("注册")
#     return render_template("long.html")

#111111
if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    app.run(debug=True, port=9989)
