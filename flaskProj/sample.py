from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Returning sample text in string format'

@app.route('/index1')
def index1():
    return '<h1>Returning sample text between html tag</h1>'

@app.route('/index2/<username>')
def index2(username):
    return f'<h1>Welcome {username}</h1>'

@app.route('/index3')
def index3():
    return render_template('sample.html')

@app.route('/index4')
def index4():
    return render_template('index.html',item_name='Sending SampleData to template')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html',items=items)

@app.route('/test')
def style_test():
    return render_template('styling.html')