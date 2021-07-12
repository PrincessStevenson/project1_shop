from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def product():
    return render_template('products.html')

@app.route('/products/new')
def new_product():
    return render_template('newproduct.html')

@app.route('/manufacturers')
def manufacturers():
    return render_template('manufacturers.html')

if __name__ == '__main__':
    app.run(debug=True)