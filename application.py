from bottle import Bottle, template, request, redirect
from database import Database

app = Bottle()
db = Database()

# Routes

@app.route('/')
def index():
    return template('index')

# Mobiles CRUD

@app.route('/mobiles')
def mobiles():
    query = "SELECT * FROM mobiles"
    result = db.fetch_all(query)
    return template('mobiles', rows=result)

@app.route('/mobiles/add', method='GET')
def add_mobile_form():
    return template('add_mobile')

@app.route('/mobiles/add', method='POST')
def add_mobile():
    brand = request.forms.get('brand')
    model = request.forms.get('model')
    price = request.forms.get('price')

    query = "INSERT INTO mobiles (brand, model, price) VALUES (?, ?, ?)"
    params = (brand, model, price)
    db.execute_query(query, params)

    redirect('/mobiles')

# Accessories CRUD

@app.route('/accessories')
def accessories():
    query = "SELECT * FROM accessories"
    result = db.fetch_all(query)
    return template('accessories', rows=result)

@app.route('/accessories/add', method='GET')
def add_accessory_form():
    return template('add_accessory')

@app.route('/accessories/add', method='POST')
def add_accessory():
    accessory_name = request.forms.get('accessory_name')
    price = request.forms.get('price')

    query = "INSERT INTO accessories (accessory_name, price) VALUES (?, ?)"
    params = (accessory_name, price)
    db.execute_query(query, params)

    redirect('/accessories')

# Static Routes
@app.route('/static/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root='./static')

# Run the application
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)

# Close the database connection when the application exits
atexit.register(db.close_connection)
