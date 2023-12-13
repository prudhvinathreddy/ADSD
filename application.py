from bottle import Bottle, route, run, template, request, redirect
import sqlite3

app = Bottle()

# SQLite Database Initialization
conn = sqlite3.connect('flower.db')
cursor = conn.cursor()

# Create flowers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS flowers (
        flower_id INTEGER PRIMARY KEY AUTOINCREMENT,
        flower_name TEXT NOT NULL,
        description TEXT NOT NULL
    )
''')

# Create colors table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS colors (
        color_id INTEGER PRIMARY KEY AUTOINCREMENT,
        color_name TEXT NOT NULL,
        flower_id INTEGER,
        FOREIGN KEY (flower_id) REFERENCES flowers(flower_id)
    )
''')

conn.commit()

# Routes

@app.route('/')
def index():
    return template('index')

# Flowers CRUD

# Modify the '/flowers' route in app.py
@app.route('/flowers')
def flowers():
    search_term = request.query.get('search', '').strip()

    # Fetch flowers based on search_term
    if search_term:
        query = "SELECT * FROM flowers WHERE flower_name LIKE ?"
        cursor.execute(query, (f"%{search_term}%",))
    else:
        query = "SELECT * FROM flowers"
        cursor.execute(query)

    result = cursor.fetchall()

    return template('flowers', rows=result, search_term=search_term)

#@app.route('/flowers')
#def flowers():
#    cursor.execute("SELECT * FROM flowers")
#    result = cursor.fetchall()
#    return template('flowers', rows=result)

@app.route('/flower_colors/<flower_id:int>')
def flower_colors(flower_id):
    # Fetch colors associated with the flower
    cursor.execute("SELECT color_name FROM colors WHERE flower_id=?", (flower_id,))
    result = cursor.fetchall()

    return template('flower_colors', flower_id=flower_id, colors=result)

@app.route('/flowers/add', method='GET')
def add_flower_form():
    return template('add_flower')

@app.route('/flowers/add', method='POST')
def add_flower():
    flower_name = request.forms.get('flower_name')
    description = request.forms.get('description')

    cursor.execute("INSERT INTO flowers (flower_name, description) VALUES (?, ?)", (flower_name, description))
    conn.commit()

    redirect('/flowers')

@app.route('/flowers/edit/<flower_id:int>', method='GET')
def edit_flower_form(flower_id):
    cursor.execute("SELECT * FROM flowers WHERE flower_id=?", (flower_id,))
    flower = cursor.fetchone()
    return template('edit_flower', flower=flower)

@app.route('/flowers/edit/<flower_id:int>', method='POST')
def edit_flower(flower_id):
    flower_name = request.forms.get('flower_name')
    description = request.forms.get('description')

    cursor.execute("UPDATE flowers SET flower_name=?, description=? WHERE flower_id=?", (flower_name, description, flower_id))
    conn.commit()

    redirect('/flowers')

@app.route('/flowers/delete/<flower_id:int>')
def delete_flower(flower_id):
    cursor.execute("DELETE FROM flowers WHERE flower_id=?", (flower_id,))
    conn.commit()

    redirect('/flowers')

# Colors CRUD

@app.route('/colors')
def colors():
    cursor.execute("SELECT * FROM colors")
    result = cursor.fetchall()
    return template('colors', rows=result)

@app.route('/colors/add', method='GET')
def add_color_form():
    # Fetch available flowers for color association
    cursor.execute("SELECT * FROM flowers")
    flowers = cursor.fetchall()
    return template('add_color', flowers=flowers)

@app.route('/colors/add', method='POST')
def add_color():
    color_name = request.forms.get('color_name')
    flower_id = request.forms.get('flower_id')

    cursor.execute("INSERT INTO colors (color_name, flower_id) VALUES (?, ?)", (color_name, flower_id))
    conn.commit()

    redirect('/colors')

@app.route('/colors/edit/<color_id:int>', method='GET')
def edit_color_form(color_id):
    cursor.execute("SELECT * FROM colors WHERE color_id=?", (color_id,))
    color = cursor.fetchone()
    
    # Fetch available flowers for color association
    cursor.execute("SELECT * FROM flowers")
    flowers = cursor.fetchall()

    return template('edit_color', color=color, flowers=flowers)

@app.route('/colors/edit/<color_id:int>', method='POST')
def edit_color(color_id):
    color_name = request.forms.get('color_name')
    flower_id = request.forms.get('flower_id')

    cursor.execute("UPDATE colors SET color_name=?, flower_id=? WHERE color_id=?", (color_name, flower_id, color_id))
    conn.commit()

    redirect('/colors')

@app.route('/colors/delete/<color_id:int>')
def delete_color(color_id):
    cursor.execute("DELETE FROM colors WHERE color_id=?", (color_id,))
    conn.commit()

    redirect('/colors')

# Static Routes
@app.route('/static/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root='./static')

# Run the application
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
