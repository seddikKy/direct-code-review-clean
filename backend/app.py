import flask
from product import DigitalProduct, PackageProduct, PromotionalProduct
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World, it's become clean now"


@app.route("/products/")
def products():
    response = flask.jsonify(
        {
            "products": [
                DigitalProduct("Digital 1", 0, 0, False).to_json(),
                DigitalProduct("Digital 2", 0, 0, True).to_json(),
                PackageProduct("Package 1", 5, 0, False).to_json(),
                PackageProduct("Package 2", 10, 0, True).to_json(),
                PromotionalProduct("Promo - Discounted Product", 0, 50, False).to_json(),
                PromotionalProduct("Promo - Free product", 0, 0, True).to_json(),
            ],    
        }        
    )

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
