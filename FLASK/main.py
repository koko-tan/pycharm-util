from flask import Flask,render_template

# 创建实例
app = Flask(__name__)


# 路由
@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('index.html')
    # return "Hello Word"


# 主函数
if __name__ == '__main__':
    app.run()