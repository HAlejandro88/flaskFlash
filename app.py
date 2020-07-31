from flask import Flask, jsonify, request

app = Flask(__name__)

from products import productos

@app.route('/ping')
def ping():
    return jsonify({"message": "holla"})


@app.route('/products', methods=['GET'])
def getPrducts():
    return jsonify(productos)


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [ product for product in productos if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"porduct": productsFound[0]})
    return jsonify({"message": "Producto no encontrado"})
        

@app.route('/productos/<string:product>')
def getAnotherProduc(product):
    print(product)
    return 'recibido desde el paremetro con puntos'


@app.route('/products', methods=['POST'])
def addproduct():
    newProduct = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quanty": request.json['quanty']
    }
    productos.append(newProduct)
    return jsonify({
        "message": "Product added succefuly",
        "products": productos
    })

@app.route('/products/<string:product_name>',  methods=['PUT'])
def updateProduct(product_name):
    productsFound = [ product for product in productos if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quanty'] =request.json['quanty']
        return jsonify({"message": "Product Update", "product": productsFound[0]})
    return jsonify({"message": "Producto no encontrado"})


if __name__ == '__main__':
    app.run(debug=True) #como segundo parametro va el puerto port=3000
