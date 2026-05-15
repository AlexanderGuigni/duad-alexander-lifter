import json

from connection import DatabaseConnection
from jwt_manager import JWT_Manager
from flask import Flask, request, Response, jsonify
from models import Products, User, create_tables, insert_initial_data, Invoice


app = Flask("user-service")
db_manager = DatabaseConnection()
jwt_manager = JWT_Manager('trespatitos', 'HS256')
user = User(db_manager)
products = Products(db_manager)
invoice = Invoice(db_manager)

def is_authenticated(request):
    token = request.headers.get('Authorization')
    if token is not None:
        token = token.replace("Bearer ", "")
        decoded = jwt_manager.decode(token)
        if decoded is not None:
            user_data = user.get_user_by_id(decoded['id'])
            if user_data is not None:
                return user_data[0]
    raise Exception({"message": "Unauthorized"}, 401)

def is_authorized(user_id):
    user_data = user.get_user_by_id(user_id)
    if user_data is not None:
        if user_data[3] == 'admin':
            return True
    raise Exception({"message": "Forbidden"}, 403)


@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None or data.get('user_role') == None or data.get('email') == None):
        return Response(status=400)
    else:
        result = user.insert_user(data.get('username'), data.get('password'), data.get('user_role'), data.get('email'))
        user_id = result

        token = jwt_manager.encode({'id':user_id})
        
        return jsonify(token=token)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(response="Bad Request", status=400)
    else:
        result = user.get_user_by_credentials(data.get('username'), data.get('password'))

        if(result == None):
            return Response(response="Unauthorized", status=401)
        else:
            user_id = result[0]
            token = jwt_manager.encode({'id':user_id})
        
            return jsonify(token=token)

@app.route('/me')
def me():
    try:
        user_id = is_authenticated(request)

        user_data = user.get_user_by_id(user_id)

        return jsonify(id=user_id, username=user_data[1])
    except Exception as e:
        return Response(response=str(e), status=500)
    
@app.route('/products', methods=['GET'])
def get_products():
    try:
        user_id = is_authenticated(request)
        is_authorized(user_id)

        products_data = products.get_all_products()
        return jsonify(products_data)
    except Exception as e:
        return Response(response=str(e), status=500)
    
@app.route('/products', methods=['POST'])
def create_product():
    try:
        user_id = is_authenticated(request)
        is_authorized(user_id)

        data = request.get_json()
        if(data.get('product_name') == None or data.get('price') == None or data.get('stock') == None):
            return Response(response="Bad Request", status=400)
        
        product_id = products.create_product(product_name=data.get('product_name'), price=data.get('price'), stock=data.get('stock'))
        return jsonify(id=product_id)
    except Exception as e:
        return Response(response=str(e), status=500)
    
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        user_id = is_authenticated(request)
        is_authorized(user_id)

        data = request.get_json()
        if(data.get('product_name') == None and data.get('price') == None and data.get('stock') == None):
            return Response(response="Bad Request", status=400)
        
        result = products.update_product(product_id, product_name=data.get('product_name'), price=data.get('price'), stock=data.get('stock'))
        if result is not None:
            return jsonify(result)
        else:
            return Response(response="Not Found", status=404)
    except Exception as e:
        return Response(response=str(e), status=500)
    
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        user_id = is_authenticated(request)
        is_authorized(user_id)

        result = products.get_product_by_id(product_id)
        if result:
            products.delete_product(product_id)
            return Response(response="Product deleted successfully", status=200)
        else:
            return Response(response="Not Found", status=404)
    except Exception as e:
        return Response(response=str(e), status=500)
    
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        user_id = is_authenticated(request)
        is_authorized(user_id)

        result = products.get_product_by_id(product_id)
        if result:
            return jsonify(result), 200
        else:
            return Response(response="Not Found", status=404)
    except Exception as e:
        return Response(response=str(e), status=500)

@app.route('/buy', methods=['POST'])
def buy_product():
    try:
        user_id = is_authenticated(request)

        data = request.get_json()
        for index,product in enumerate(data):
            if(product.get('id') == None or product.get('quantity') == None):
                return Response(response="Bad Request: Missing product_id or quantity in one or more products", status=400)
            product_data = products.get_product_by_id(product.get('id'))
            if product_data is None:
                return Response(response=f"Bad Request: Product with id {product.get('id')} not found", status=400)
            elif product_data['stock'] < product.get('quantity'):
                return Response(response=f"Bad Request: Not enough stock for product with id {product.get('id')}", status=400)
            else:
                data[index]["price"] = product_data.get("price")
        
        result = invoice.genetate_invoice(user_id, data)
        if result is not None:
            return jsonify(result), 200
        else:
            return Response(response="Not Found", status=404)
    except Exception as e:
        return Response(response=str(e), status=500)
    
@app.route('/invoices/<int:invoice_id>', methods=['GET'])
def get_invoice_by_id(invoice_id):
    try:
        user_id = is_authenticated(request)

        result = invoice.get_invoice_by_id(invoice_id)
        if result:
            return jsonify(result), 200
        else:
            return Response(response="Not Found", status=404)
    except Exception as e:
        return Response(response=str(e), status=500)

@app.route('/invoices/user/<int:user_id>', methods=['GET'])
def get_invoices_by_user_id(user_id):
    try:
        user_id = is_authenticated(request)

        result = invoice.get_invoices_by_user_id(user_id)
        if result:
            return jsonify(result), 200
        else:
            return Response(response="Not Found", status=404)
    except Exception as e:
        return Response(response=str(e), status=500)

if __name__ == "__main__":
    #create_tables(db_manager.engine)
    #insert_initial_data(db_manager)
    app.run(debug=True, host='localhost', port=5000)