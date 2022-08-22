from flask import Flask, current_app, g, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, Flaskbook!"


@app.route("/hello/<string:name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello World! {name}"


@app.route("/name/<string:name>")
def show_name(name: str):
    return render_template("index.html", name=name)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # TODO: メールを送る

        # contactエンドポイントへリダイレクトする
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")


with app.test_request_context():
    # to /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=1
    print(url_for("show_name", name="ichiro", page="1"))

# アプリケーションコンテキストを取得してスタックへpushする
ctx = app.app_context()
ctx.push()

# current_appにアクセスが可能になる
print(current_app.name)

# globalなテンポラリ領域に値を設定する
g.connection = "connection"
print(g.connection)
