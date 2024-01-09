from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "Каталог", "url": "catalog"},
    {"name": "Личный кабинет", "url": "account"},
]

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title="Главная", menu=menu)

@app.route("/catalog")
def catalog():
    return render_template('catalog.html', title="Каталог", menu=menu)

@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"

@app.route("/account", methods=["POST", "GET"])
def account():
    if request.method == 'POST':
        print(request.form)
    return render_template('account.html', title="Личный кабинет", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)